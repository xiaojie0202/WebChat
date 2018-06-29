from bs4 import BeautifulSoup
from app import session
import base64
import requests
from io import BytesIO


# 解析点击确认登陆后获取的凭证
def xml_parse(text):
    dic = {}
    soup = BeautifulSoup(text, 'lxml')
    div_erro = soup.find(name='error')
    for item in div_erro.find_all(recursive=False):
        dic[item.name] = item.text

    return dic


def img_base64(url):
    url = 'https://wx.qq.com' + url
    cookies = session.get('cookies')
    response = requests.get(url=url, cookies=cookies)
    img = base64.b64encode(response.content)
    img = img.decode('utf-8')
    img = 'data:image/jpg;base64,' + img
    print(img)
    return img


'''
"BaseResponse": {
"Ret": 1101,
"ErrMsg": ""
}
'''

user_info = {
    'BaseResponse': {'Ret': 0, 'ErrMsg': ''},
    'Count': 11,
    'ContactList': [
        ###################好友
        {'Uin': 0,
         'UserName': '@822627c422a1621961a04e651a8811a34724bfe1a36760b400095021484c71f6',
         'NickName': '喜洋洋',
         'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=679541338&username=@822627c422a1621961a04e651a8811a34724bfe1a36760b400095021484c71f6&skey=@crypt_9d36bb3d_55328cc31f593ce6a790c5f68dee5921',
         'ContactFlag': 98563,
         'MemberCount': 0,
         'MemberList': [],
         'RemarkName': '中科_马丹',
         'HideInputBarFlag': 0,
         'Sex': 0,
         'Signature': 'g', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'XYY', 'PYQuanPin': 'xiyangyang',
         'RemarkPYInitial': '', 'RemarkPYQuanPin': '', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0,
         'AttrStatus': 4901, 'Province': '天津', 'City': '河北', 'Alias': '', 'SnsFlag': 1, 'UniFriend': 0,
         'DisplayName': '',
         'ChatRoomId': 0, 'KeyWord': '', 'EncryChatRoomId': '', 'IsOwner': 0},

        #########################群组
        {'Uin': 0,
         'UserName': '@@bdb02dbd8ae61ecb3cb3c5cca53381308998bd482722bdf72baa76401c3cf079',
         'NickName': '一家四口<span class="emoji emoji1f44c"></span>',
         'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgetheadimg?seq=0&username=@@bdb02dbd8ae61ecb3cb3c5cca53381308998bd482722bdf72baa76401c3cf079&skey=@crypt_9d36bb3d_55328cc31f593ce6a790c5f68dee5921',
         'ContactFlag': 0,
         'MemberCount': 4,
         'MemberList': [
             {'Uin': 0, 'UserName': '@566b9753b2feb7a6e8d5417d60164bf554f1594c8d4dac97a918691b38b2cc90', 'NickName': '',
              'AttrStatus': 0, 'PYInitial': '', 'PYQuanPin': '', 'RemarkPYInitial': '', 'RemarkPYQuanPin': '',
              'MemberStatus': 0, 'DisplayName': '', 'KeyWord': ''},

             {'Uin': 0, 'UserName': '@d0b475cf2e57e99b784131e0255957cb713c0035636d2d5c9d560d611760572f', 'NickName': '',
              'AttrStatus': 0, 'PYInitial': '', 'PYQuanPin': '', 'RemarkPYInitial': '', 'RemarkPYQuanPin': '',
              'MemberStatus': 0, 'DisplayName': '', 'KeyWord': ''},

             {'Uin': 0, 'UserName': '@66549e43468e03eeb87f7ae84a610600c1e60ec1a3193c260c17c570eba98b50', 'NickName': '',
              'AttrStatus': 0, 'PYInitial': '', 'PYQuanPin': '', 'RemarkPYInitial': '', 'RemarkPYQuanPin': '',
              'MemberStatus': 0, 'DisplayName': '', 'KeyWord': ''},

             {'Uin': 0, 'UserName': '@1c49e471cbbca42dc21d75d46be03595bc2a63a5d4ae2243c30a1a18da55e080', 'NickName': '',
              'AttrStatus': 0, 'PYInitial': '', 'PYQuanPin': '', 'RemarkPYInitial': '', 'RemarkPYQuanPin': '',
              'MemberStatus': 0, 'DisplayName': '', 'KeyWord': 'wan'}
         ],
         'RemarkName': '',
         'HideInputBarFlag': 0,
         'Sex': 0,
         'Signature': '', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': '', 'PYQuanPin': '', 'RemarkPYInitial': '',
         'RemarkPYQuanPin': '', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 1, 'AttrStatus': 0, 'Province': '',
         'City': '', 'Alias': '', 'SnsFlag': 0, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '',
         'EncryChatRoomId': '', 'IsOwner': 0},
    ],

    'SyncKey':
        {'Count': 4,
         'List':
             [
                 {'Key': 1, 'Val': 679548119},
                 {'Key': 2, 'Val': 679548181},
                 {'Key': 3, 'Val': 679547976},
                 {'Key': 1000, 'Val': 1529658962}
             ]
         },
    ####################个人信息
    'User':
        {'Uin': 2365688641,
         'UserName': '@1c49e471cbbca42dc21d75d46be03595bc2a63a5d4ae2243c30a1a18da55e080',
         'NickName': '小杰',
         'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=818519790&username=@1c49e471cbbca42dc21d75d46be03595bc2a63a5d4ae2243c30a1a18da55e080&skey=@crypt_9d36bb3d_55328cc31f593ce6a790c5f68dee5921',
         'RemarkName': '',
         'PYInitial': '',
         'PYQuanPin': '',
         'RemarkPYInitial': '',
         'RemarkPYQuanPin': '',
         'HideInputBarFlag': 0,
         'StarFriend': 0,
         'Sex': 1,
         'Signature': '',
         'AppAccountFlag': 0,
         'VerifyFlag': 0,
         'ContactFlag': 0,
         'WebWxPluginSwitch': 0,
         'HeadImgFlag': 1,
         'SnsFlag': 17
         },
    'ChatSet': 'filehelper,weixin,@6dd0c3f70d4b06873bbe0ae75f1cd6d401a215171f0164d412505028ce32b46e,@4579cf957390c5edc746117bc823bd3cefd00aa50be9abd2b94f167c272635a0,@a15dcdde898f3da8fabe598d1cda4ff6,@822627c422a1621961a04e651a8811a34724bfe1a36760b400095021484c71f6,@@e3b140553c22257963a62de7e1e7ddcfe8684880c9d59054167df1738f193376,@@bdb02dbd8ae61ecb3cb3c5cca53381308998bd482722bdf72baa76401c3cf079,filehelper,@@5478159241d40651d6ab16dc72d380346264d18c29615690ea21b39f2f10adf4,fmessage,@@785a63e6a3e738ac26d06dc7c53aaf8a39776db6945ee148e77ea01c40fc8bcb,',
    'SKey': '@crypt_9d36bb3d_55328cc31f593ce6a790c5f68dee5921',
    'ClientVersion': 369493793,
    'SystemTime': 1529683552,
    'GrayScale': 1,
    'InviteStartCount': 40,
    'MPSubscribeMsgCount': 6,

    ######################公众号信息
    'MPSubscribeMsgList': [
        {
            'UserName': '@9dc69a1d90ec2b798f9223b7f1c4f613',
            'MPArticleCount': 5,
            'MPArticleList':
                [
                    {
                        'Title': '男人向往的爱情是什么？',
                        'Digest': '阅读本文前，请您先点击上面的蓝色字体“情感生活心理学”，再点击“关注”，这样您就可以继续免费收到超精彩的文章',
                        'Cover': 'http://mmbiz.qpic.cn/mmbiz/bVysP9ny79CjKoJgjWT9cWId6lmgYqlp7dic7GjxY7PutmymNHqXI7CwQqpVaEcFpL4BSQPjHnEmR524sjLrb1A/640?wxtype=jpeg&wxfrom=0',
                        'Url': 'http://mp.weixin.qq.com/s?__biz=MjM5MzA0MzQwMA==&mid=2650642248&idx=1&sn=20b395a69d79a569478bef917665b577&chksm=be9431ef89e3b8f99b010045f3ac498d2af1a2e8ee016331eace739574102f73a3695e874e0f&scene=0#rd'
                    },

                    {'Title': '爱情不是1+1=2，而是0.5+0.5=1',
                     'Digest': '阅读本文前，请您先点击上面的蓝色字体“情感生活心理学”，再点击“关注”，这样您就可以继续免费收到超精彩的文章',
                     'Cover': 'http://mmbiz.qpic.cn/mmbiz/bVysP9ny79CjKoJgjWT9cWId6lmgYqlpN5kOicrodCUgl2s8uiaLYGyNIjbKHwlQicr1rYGKpBF4WuJKicSrKoVUlg/300?wxtype=jpeg&wxfrom=0',
                     'Url': 'http://mp.weixin.qq.com/s?__biz=MjM5MzA0MzQwMA==&mid=2650642248&idx=2&sn=f0a298dec05e2e19ab6bfa4daa9a5b73&chksm=be9431ef89e3b8f96d2ce568e82b13dbb3c1c78e11f058914398d3c45d016db864ef6e79abdf&scene=0#rd'},

                    {'Title': '生活可以没有爱情，爱情却是要去过生活的。',
                     'Digest': '阅读本文前，请您先点击上面的蓝色字体“情感生活心理学”，再点击“关注”，这样您就可以继续免费收到超精彩的文章',
                     'Cover': 'http://mmbiz.qpic.cn/mmbiz/bVysP9ny79CjKoJgjWT9cWId6lmgYqlpxwibziaS4R8sQuLf2jwuJH6OicOo58HdIokyvIGcYUltZR6q1B82nDUTw/300?wxtype=jpeg&wxfrom=0',
                     'Url': 'http://mp.weixin.qq.com/s?__biz=MjM5MzA0MzQwMA==&mid=2650642248&idx=3&sn=6566800ae9b829ad8c8f10cae236357d&chksm=be9431ef89e3b8f9326923bc636f8d0720d6195f8bf5c30ac3ea0e4ce015ef8f13d7031458d5&scene=0#rd'},

                    {'Title': '不要为了成全爱情，委屈了自己！', 'Digest': '阅读本文前，请您先点击上面的蓝色字体“情感生活心理学”，再点击“关注”，这样您就可以继续免费收到超精彩的文章',
                     'Cover': 'http://mmbiz.qpic.cn/mmbiz/bVysP9ny79CjKoJgjWT9cWId6lmgYqlpBE3LMEatBJym0cOWVpx0yicsWUpUkm9D5sV8xfuxPHtlRBibwXHBUZ6g/300?wxtype=jpeg&wxfrom=0',
                     'Url': 'http://mp.weixin.qq.com/s?__biz=MjM5MzA0MzQwMA==&mid=2650642248&idx=4&sn=9317349e4a69a313082cd4a4010cfa1d&chksm=be9431ef89e3b8f95deec6bc86b1952733a7c6b975b4f4a8c11856f1401a48de979dfe43b916&scene=0#rd'},

                    {'Title': '找老婆，一定要找手脚冰冷的人！', 'Digest': '阅读本文前，请您先点击上面的蓝色字体“情感生活心理学”，再点击“关注”，这样您就可以继续免费收到超精彩的文章',
                     'Cover': 'http://mmbiz.qpic.cn/mmbiz/bVysP9ny79CjKoJgjWT9cWId6lmgYqlpuibE0HsQfAIzZ3xp4zf7WZTWMzHBWoicAzQgnDvxIR7mtxwu4LQcFLzw/300?wxtype=jpeg&wxfrom=0',
                     'Url': 'http://mp.weixin.qq.com/s?__biz=MjM5MzA0MzQwMA==&mid=2650642248&idx=5&sn=fa4cb0947170412ce5d78a7ce4c1241c&chksm=be9431ef89e3b8f995958903a5c1db076b9f0007b82095b5de47260281b9b2a444d974115729&scene=0#rd'}
                ],
            'Time': 1529683415,
            'NickName': '情感生活心理学'
        },

        {
            'UserName': '@183404dc5a68a1aca1aa4feb767f9dad', 'MPArticleCount': 5,
            'MPArticleList': [
                {'Title': '流量漫游取消=不被“薅羊毛”？', 'Digest': '运营商该薅的羊毛还是会薅，要想得到真正利好，恐怕还得等等……',
                 'Cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/YTI67xfsN507d6vbYJuFt5A6qxtkkzTKAy9ZGPpEZnkQaicghPEjetyuyibzpMtEknht0tIUgdmzicshYXyPkQEYg/640?wxtype=jpeg&wxfrom=0',
                 'Url': 'http://mp.weixin.qq.com/s?__biz=MjM5Mzg4NzExMQ==&mid=2651201611&idx=1&sn=27c9bb675c6cd935b8e94cefefb9115f&chksm=bd62a6a38a152fb56f177f98e41a5a09b36284b91275ec0671ca007678dc9ef85c1eb141db40&scene=0#rd'},
                {'Title': '不懂拍照怎么构图？从这篇学起', 'Digest': '大部分关于构图的教程，基本上都是罗列出一些法则，今天，IT之家小编就对于摄影构图，来谈一些自己的理解。',
                 'Cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/YTI67xfsN507d6vbYJuFt5A6qxtkkzTK8icclLppDlpb5miaAdEfqiaMa1K19Sj0RIH8sTSStjSRaicYn5WShKWQXg/300?wxtype=jpeg&wxfrom=0',
                 'Url': 'http://mp.weixin.qq.com/s?__biz=MjM5Mzg4NzExMQ==&mid=2651201611&idx=2&sn=a643be7b38f06686f51cefbecd756929&chksm=bd62a6a38a152fb50a400b9b8e7747e17b816732178c58bacdbab45f18294adbefb2d4b49d5b&scene=0#rd'},
                {'Title': '今日神评：青春版和畅玩版还能这么理解？角度刁钻！', 'Digest': 'IT之家，看的就是评论！',
                 'Cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/YTI67xfsN5261aNlGD42kibaQC7KvTxic8qGKmUbqnBP6lzNXlweHQbkiaHq7YOyIOek7PgS1CWggrYAXuT26Tm3A/300?wxtype=jpeg&wxfrom=0',
                 'Url': 'http://mp.weixin.qq.com/s?__biz=MjM5Mzg4NzExMQ==&mid=2651201611&idx=3&sn=a386d9c728d9e03bb96b5d589e3ba9ba&chksm=bd62a6a38a152fb5ec2e77fb51e4e0ac4d26ddd3b37e805525b77c725f5253a2b6d315e395ef&scene=0#rd'},
                {'Title': '唯一千方百计借钱给我的，也就这位仁兄了……', 'Digest': '支付宝上线了一个“500元备用金”贴心功能，蚂蚁黄金会员以上可以使用，另外芝麻信用分也不能低于650',
                 'Cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/YTI67xfsN507d6vbYJuFt5A6qxtkkzTKlxZrqAPDfVL475kTgF4NG9D0sTd7RPlS0xicmBhSMkHnKoHDpAzn7yA/300?wxtype=jpeg&wxfrom=0',
                 'Url': 'http://mp.weixin.qq.com/s?__biz=MjM5Mzg4NzExMQ==&mid=2651201611&idx=4&sn=fef0f7195ef5651facf5519a7fc533aa&chksm=bd62a6a38a152fb5fb2a47e98257e8b00b746137dd2092bdf7add130d097bf35fe85a8d7779a&scene=0#rd'},
                {'Title': '# 一日辣榜 #别管音响还是灯泡，反正你要的是情调！', 'Digest': '火辣的商品，火辣的价格，辣品告诉你什么值得买，帮你赚尽便宜！',
                 'Cover': 'http://mmbiz.qpic.cn/mmbiz_jpg/YTI67xfsN507d6vbYJuFt5A6qxtkkzTK3ulLIkxUpIicty0S54puOec7TFDBSAw1A2o0Dwxnibde7z4zOXkrKImw/300?wxtype=jpeg&wxfrom=0',
                 'Url': 'http://mp.weixin.qq.com/s?__biz=MjM5Mzg4NzExMQ==&mid=2651201611&idx=5&sn=90667e228db2acce12e8e0248ce045bc&chksm=bd62a6a38a152fb592f9b808f201f7a79271924228f65dd1ce4647bf9b7befee3cad5e060fa5&scene=0#rd'}],
            'Time': 1529676437,
            'NickName': 'IT之家'
        },

    ],
    'ClickReportInterval': 600000}

# user_info['ContactList'] # 好友信息,包括群组
# user_info['User'] # 个人信息
# user_info['MPSubscribeMsgList'] # 公众号信息
# getmsg['AddMsgList']
get_msg = {
    'BaseResponse': {'Ret': 0, 'ErrMsg': ''},
    'AddMsgCount': 1,
    'AddMsgList':
        [
            {
                'FromUserName': '@2c78a478388f8b2c6790b058e6c914e8c8ce010a9823b31201fba5be87a87b79',  # 给你发消息的username
                'ToUserName': '@6db116c83b9f5b4a19f83b11199e8ed6948907fde6430dcc8626cb930fd12ad5',  # 自己的usernae
                'MsgType': 1,
                'Content': '军训',
                'Status': 3,
                'ImgStatus': 1,
                'CreateTime': 1529729558,
                'AppMsgType': 0,
                'NewMsgId': 8376265974577126738,
            }
        ],
}
# {'BaseResponse': {'Ret': 0, 'ErrMsg': ''}, 'AddMsgCount': 1, 'AddMsgList': [{'MsgId': '7939179473651192182', 'FromUserName': '@977c95b99b5e3ccf4c59a34496b5d37ba21bd540daa5aa5dd07c9ac1d3d1fef2', 'ToUserName': '@d8139643494d32119a1432758a6b0c8e9834aca4a77bc9e0d16af4561b35499b', 'MsgType': 1, 'Content': '2', 'Status': 3, 'ImgStatus': 1, 'CreateTime': 1529734625, 'VoiceLength': 0, 'PlayLength': 0, 'FileName': '', 'FileSize': '', 'MediaId': '', 'Url': '', 'AppMsgType': 0, 'StatusNotifyCode': 0, 'StatusNotifyUserName': '', 'RecommendInfo': {'UserName': '', 'NickName': '', 'QQNum': 0, 'Province': '', 'City': '', 'Content': '', 'Signature': '', 'Alias': '', 'Scene': 0, 'VerifyFlag': 0, 'AttrStatus': 0, 'Sex': 0, 'Ticket': '', 'OpCode': 0}, 'ForwardFlag': 0, 'AppInfo': {'AppID': '', 'Type': 0}, 'HasProductId': 0, 'Ticket': '', 'ImgHeight': 0, 'ImgWidth': 0, 'SubMsgType': 0, 'NewMsgId': 7939179473651192182, 'OriContent': '', 'EncryFileName': ''}], 'ModContactCount': 0, 'ModContactList': [], 'DelContactCount': 0, 'DelContactList': [], 'ModChatRoomMemberCount': 0, 'ModChatRoomMemberList': [], 'Profile': {'BitFlag': 0, 'UserName': {'Buff': ''}, 'NickName': {'Buff': ''}, 'BindUin': 0, 'BindEmail': {'Buff': ''}, 'BindMobile': {'Buff': ''}, 'Status': 0, 'Sex': 0, 'PersonalCard': 0, 'Alias': '', 'HeadImgUpdateFlag': 0, 'HeadImgUrl': '', 'Signature': ''}, 'ContinueFlag': 0, 'SyncKey': {'Count': 8, 'List': [{'Key': 1, 'Val': 679548261}, {'Key': 2, 'Val': 679548314}, {'Key': 3, 'Val': 679548207}, {'Key': 11, 'Val': 679548027}, {'Key': 201, 'Val': 1529734625}, {'Key': 1000, 'Val': 1529731322}, {'Key': 1001, 'Val': 1529731394}, {'Key': 2001, 'Val': 1529480143}]}, 'SKey': '', 'SyncCheckKey': {'Count': 8, 'List': [{'Key': 1, 'Val': 679548261}, {'Key': 2, 'Val': 679548314}, {'Key': 3, 'Val': 679548207}, {'Key': 11, 'Val': 679548027}, {'Key': 201, 'Val': 1529734625}, {'Key': 1000, 'Val': 1529731322}, {'Key': 1001, 'Val': 1529731394}, {'Key': 2001, 'Val': 1529480143}]}}
import time

for msg in get_msg['AddMsgList']:
    FromUserName = msg['FromUserName']
    Content = msg['Content']
    ctime = time.strftime('%H:%S', time.localtime(msg['CreateTime']))

qz_msg = {
    'BaseResponse': {'Ret': 0, 'ErrMsg': ''},
    'AddMsgCount': 1,
    'AddMsgList':
        [
            {
                'FromUserName': '@@82b9ab229fb0d1397e6504d0616510fad9cab214d14fb497e4d7cce2bf3e37a7',
                'ToUserName': '@6db116c83b9f5b4a19f83b11199e8ed6948907fde6430dcc8626cb930fd12ad5',
                'MsgType': 1,
                'Content': '@2c78a478388f8b2c6790b058e6c914e8c8ce010a9823b31201fba5be87a87b79:<br/>3',
                'Status': 3,
                'ImgStatus': 1,
                'AppMsgType': 0,
                'CreateTime': 1529730202,
                'NewMsgId': 2975838453317337755,
            }
        ]
}

gzh_msg = {'BaseResponse': {'Ret': 0, 'ErrMsg': ''},
           'AddMsgCount': 1,
           'AddMsgList':
               [
                   {
                       'MsgId': '7333935059521947665',
                       'FromUserName': '@6bd4712b7756a6b6c097ebea9969ca62',
                       'ToUserName': '@d8139643494d32119a1432758a6b0c8e9834aca4a77bc9e0d16af4561b35499b',
                       'MsgType': 49,
                       'Status': 3,
                       'ImgStatus': 1,
                       'CreateTime': 1529733593,
                       'FileName': '抽签还打5.8折！火爆成都的串串跑来"诱惑"天津吃货了！折后不到4毛！',
                       'Url': 'http://mp.weixin.qq.com/s?__biz=MzI4ODE0MDc5MA==&amp;mid=2651819644&amp;idx=1&amp;sn=88d7c7a745b08c3294543088f17c0bdc&amp;chksm=f039d2e5c74e5bf3da8cc139a7dcc510f5854b0b3cbb2e5dab2a9ecad16327fa9be12b6d236d&amp;scene=0#rd',
                       'AppMsgType': 5,
                       'NewMsgId': 7333935059521947665,
                   }
               ],

           }
'''



{
    'msgtype': 3, 
    'FromUserName': '@297b04adf91f1fbc591fbee94c17bfc9', 
    'ctime': '19:36', 
    'title': '为您搜索到498553个"134"相关商品', 
    'Content': '.....................',
    'url': 'http://wq.jd.com/search/search?key=134&amp;PTAG=17005.11.1'
}

'''