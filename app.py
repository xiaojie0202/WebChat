from flask import Flask, request, render_template, session, jsonify, make_response, redirect, url_for, Response
from bs4 import BeautifulSoup
from utils import xml_parse, img_base64
import requests
import time
import re
import json

app = Flask(__name__)
app.debug = True
app.secret_key = 'sadkhj@#$2^Agfasg!@%'


@app.route('/')
def index():
    # 获取微信登陆后的初始化信息
    ticket_dict = session.get('ticket_dic')
    cookies = session.get('cookies')
    if not ticket_dict:
        return redirect(url_for(endpoint='login'))
    url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-674270211&lang=zh_CN&pass_ticket={0}".format(
        ticket_dict.get('pass_ticket'))
    data_dict = {
        "BaseRequest":
            {
                "Uin": ticket_dict.get('wxuin'),
                "Sid": ticket_dict.get('wxsid'),
                "Skey": ticket_dict.get('skey'),
                "DeviceID": "e687896895614144"
            }
    }
    init_info = requests.post(url=url, json=data_dict)
    init_info.encoding = 'utf-8'
    init_dict = init_info.json()

    if init_dict['BaseResponse']['Ret'] != 0:
        return redirect(url_for(endpoint='login'))

    session['SyncKey'] = init_dict['SyncKey']
    # 获取所有的联系人
    user_list_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&r={0}&seq=0&skey={1}".format(int(time.time()*1000), ticket_dict.get('skey'))
    user_list_ret = requests.get(url=user_list_url, cookies=cookies)
    user_list_ret.encoding = 'utf-8'
    user_list_dict = user_list_ret.json()
    return render_template('index.html', init_dict=init_dict, img_base64=img_base64, user_dict=user_list_dict)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # 获取微信扫描登陆的二维码, 响应信息 window.QRLogin.code = 200; window.QRLogin.uuid = "AeMwX5ZZ1A==";
        wx_response = requests.get(
            url="https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}".format(
                int(time.time() * 1000)))
        # 解析出来图片的UUID
        uuid = re.search(r'uuid = "(?P<uuid>.+)";', wx_response.text).group('uuid')
        # 把二维码UUID拼接成图片连接
        img_url = 'https://login.weixin.qq.com/qrcode/' + uuid
        session['uuid'] = uuid
        return render_template('login.html', img=img_url)


@app.route('/check_login', methods=['GET', 'POST'])
def check_login():
    '''
    长轮询查询是否扫描，登陆

    没有扫描返回 ： window.code=408;
    二维码超时 ： window.code=400;
    扫码后返回头像： window.code=201;window.userAvatar = 头像图片
    点击确认登陆后返回window.code=200;window.redirect_uri=跳转url

    :return:
    '''
    if request.method == 'GET':
        data = {'code': 408}
        uuid = session.get('uuid')
        # 长轮询请求检测是否扫码或者登陆
        check_url = "https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip=0&r=-639143436&_={1}".format(
            uuid, int(time.time() * 1000))
        check_response = requests.get(url=check_url)
        # code=201 代表已经扫码, 把用户头像返回给前端
        if 'code=201' in check_response.text:
            data['code'] = 201
            img_src = re.search(r"userAvatar = '(?P<src>.+)';", check_response.text).group('src')
            data['src'] = img_src
        # code=400代表二维码超时
        elif 'code=400' in check_response.text:
            data['code'] = 400
        # code=200 代表点击了确认登陆
        elif 'code=200' in check_response.text:
            data['code'] = 200
            redirect_url = re.search(r'redirect_uri="(?P<url>.+)";', check_response.text).group('url')
            data['url'] = redirect_url + '&fun=new&version=v2'
            # 访问微信服务器返回过来的重定向url,并访问此url获取凭证
            ticket_response = requests.get(url=data['url'])
            # 把xml解析成字典
            ticket_dict = xml_parse(ticket_response.text)
            session['ticket_dic'] = ticket_dict
            session['cookies'] = ticket_response.cookies.get_dict()
        return jsonify(data)


@app.route('/send',methods=['GET','POST'])
def send():
    ticket_dict = session.get('ticket_dic')

    from_user = request.form.get('formuser')
    to = request.form.get('to')
    content = request.form.get('content')
    ctime = str(time.time()*1000)
    msg_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket={0}".format(ticket_dict['pass_ticket'])

    data_dict = {
        'BaseRequest': {
            "DeviceID": "e687896895614144",
            "Sid": ticket_dict.get('wxsid'),
            "Uin": ticket_dict.get('wxuin'),
            "Skey": ticket_dict.get('skey'),
        },
        'Msg': {
            'ClientMsgId':ctime,
            'LocalID':ctime,
            'FromUserName':from_user,
            'ToUserName':to,
            "Content":content,
            'Type':1
        },
        'Scene': 0
    }

    ret = requests.post(
        url=msg_url,
        data=bytes(json.dumps(data_dict,ensure_ascii=False),encoding='utf-8')
    )
    return jsonify(ret.json())


@app.route('/getmsg', methods=['GET', 'POST'])
def get_msg():
    # 检查是否有新消息到来
    sync_url = "https://webpush.weixin.qq.com/cgi-bin/mmwebwx-bin/synccheck"
    ticket_dict = session.get('ticket_dic')
    sync_data_list = []
    for item in session.get('SyncKey')['List']:
        temp = "%s_%s" % (item['Key'], item['Val'])
        sync_data_list.append(temp)

    sync_data_str = "|".join(sync_data_list)
    nid = int(time.time())
    sync_dict = {
        "r": nid,
        "skey": ticket_dict['skey'],
        "sid": ticket_dict['wxsid'],
        "uin": ticket_dict['wxuin'],
        "deviceid": "e531777446530354",
        "synckey": sync_data_str
    }
    response_sync = requests.get(sync_url, params=sync_dict, cookies=session.get('cookies'))
    print(response_sync.text)
    # window.synccheck={retcode:"0",selector:"2"}
    if 'selector:"2"' in response_sync.text:
        fetch_msg_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsync?sid=%s&skey=%s&lang=zh_CN&pass_ticket=%s" % (ticket_dict['wxsid'], ticket_dict['skey'], ticket_dict['pass_ticket'])

        form_data = {
            'BaseRequest': {
                'DeviceID': 'e531777446530354',
                'Sid': ticket_dict['wxsid'],
                'Skey': ticket_dict['skey'],
                'Uin': ticket_dict['wxuin']
            },
            'SyncKey': session.get('SyncKey'),
            'rr': str(time.time())
        }
        response_fetch_msg = requests.post(fetch_msg_url, json=form_data)
        response_fetch_msg.encoding = 'utf-8'
        res_fetch_msg_dict = json.loads(response_fetch_msg.text)
        session['SyncKey'] = res_fetch_msg_dict['SyncKey']
        '''
        msgtype:1 :个人信息
        msgtypy:2: 群组消息
        msgtype:3: 公众号信息
        '''
        msg = {'msg': True, 'data':[]}
        print()
        if not res_fetch_msg_dict['AddMsgList']:
            return jsonify({'msg': False})
        for item in res_fetch_msg_dict['AddMsgList']:
            msg_dict = {'msgtype': 1, 'Content': item['Content'], 'FromUserName': item['FromUserName'], 'ctime': time.strftime('%H:%S', time.localtime(item['CreateTime']))}

            if item['Url'] != '':
                msg_dict['msgtype'] = 3
                msg_dict['title'] = item['FileName']
                msg_dict['url'] = item['Url']
            if item['FromUserName'].count('@') == 2:
                msg_dict['msgtype'] = 2
                send_user, info = re.search(r'(?P<senduser>.+):<br/>(?P<msg>.+)', msg_dict['Content']).group('senduser', 'msg')
                msg_dict['SendUser'] = send_user
                msg_dict['Content'] = info

            print(msg_dict)
            msg['data'].append(msg_dict)
            print(item['Content'], ":::::", item['FromUserName'], "---->", item['ToUserName'], )
        return jsonify(msg)
    return jsonify({'msg': False})

if __name__ == '__main__':
    app.run()
