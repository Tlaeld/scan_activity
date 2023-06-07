import asyncio
import json
import re
from telegram import Bot
import requests
import json
import time
from functools import partial
print = partial(print, flush=True)
# 获取当前文件位置
import os

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

with open("./config/bot.json", 'r', encoding='utf-8') as f:
    BOT = json.load(f)

my_bot_id = int(BOT['bot_token'].split(":")[0])
need_proxy = BOT['need_proxy']
group_id = int(BOT['group_id'])

LZ_TOKEN_KEY = ''
LZ_TOKEN_VALUE = ''
AUTH_C_USER = ''
LZ_AES_PIN = ''
JSESSIONID = ''

PATH = os.path.dirname(os.path.abspath(__file__))

nummax = 15

if need_proxy:
    try:
        proxy = BOT['proxy']
        os.environ['ALL_PROXY'] = proxy
        bot = Bot(token=BOT['bot_token'])
    except Exception as e:
        print(e)
        proxy = None
        print("代理配置错误")
        exit()
else:
    bot = Bot(token=BOT['bot_token'])



def post(url, data, headers,_cookies="",flag=0):
    global LZ_AES_PIN
    global LZ_TOKEN_KEY
    global LZ_TOKEN_VALUE
    global JSESSIONID
    global AUTH_C_USER  
    try:
        if (_cookies):
            response = requests.post(url, data=data, headers=headers,cookies=_cookies)
        elif (flag == 1):
            response = requests.post(url, data=data, headers=headers)
        else:
            response = requests.post(url, data=data, headers=headers)
        if (response.cookies.get('LZ_AES_PIN')):
            LZ_AES_PIN = response.cookies.get('LZ_AES_PIN')
        if (response.cookies.get('JSESSIONID')):
            JSESSIONID = response.cookies.get('JSESSIONID')
        if (response.cookies.get('LZ_TOKEN_KEY')):
            LZ_TOKEN_KEY = response.cookies.get('LZ_TOKEN_KEY')
        if (response.cookies.get('LZ_TOKEN_VALUE')):
            LZ_TOKEN_VALUE = response.cookies.get('LZ_TOKEN_VALUE')
        if (response.cookies.get('AUTH_C_USER')):
            AUTH_C_USER = response.cookies.get('AUTH_C_USER')
        return response
    except Exception as e:
        print(e)

def get(url, headers,_cookies="",flag=0):
    global LZ_AES_PIN
    global LZ_TOKEN_KEY
    global LZ_TOKEN_VALUE
    global JSESSIONID
    global AUTH_C_USER
    try:
        if (_cookies):
            response = requests.get(url,headers=headers,cookies=_cookies)
        elif (flag == 1):
            response = requests.get(url,headers=headers)
        else:
            response = requests.get(url, headers=headers)
        if (response.cookies.get('LZ_AES_PIN')):
            LZ_AES_PIN = response.cookies.get('LZ_AES_PIN')
        if (response.cookies.get('JSESSIONID')):
            JSESSIONID = response.cookies.get('JSESSIONID')
        if (response.cookies.get('LZ_TOKEN_KEY')):
            LZ_TOKEN_KEY = response.cookies.get('LZ_TOKEN_KEY')
        if (response.cookies.get('LZ_TOKEN_VALUE')):
            LZ_TOKEN_VALUE = response.cookies.get('LZ_TOKEN_VALUE')
        if (response.cookies.get('AUTH_C_USER')):
            AUTH_C_USER = response.cookies.get('AUTH_C_USER')
        return response
    except Exception as e:
        print(e)

def init_User(cookies,pt_pin):
    try:
        global LZ_AES_PIN
        global LZ_TOKEN_KEY
        global LZ_TOKEN_VALUE
        global JSESSIONID
        global AUTH_C_USER
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': UA,
            'Cookie': cookies,
            'Host': 'api.m.jd.com',
            'Accept': '*/*',
        }
        url = "https://api.m.jd.com/client.action?functionId=isvObfuscator&body=%7B%22url%22%3A%22https%3A%2F%2Flzkj-isv.isvjcloud.com%22%2C%22id%22%3A%22%22%7D&ef=1&ep=%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1681722802716%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22d_brand%22%3A%22J1LGJm%3D%3D%22%2C%22screen%22%3A%22EJKmoNO2CNK%3D%22%2C%22area%22%3A%22C182C182DJCnXzO%3D%22%2C%22uuid%22%3A%22YzTrEJG1YWHuZtOyDQDrYJu3CJDwCzO5DtSyYzGzYzG%3D%22%2C%22osVersion%22%3A%22Dy4nBtS%3D%22%2C%22d_model%22%3A%22UODCJJOm%22%2C%22aid%22%3A%22YzTrEJG1YWHuZtOyDQDrYJu3CJDwCzO5DtSyYzGzYzG%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D&client=android&clientVersion=11.4.2&uuid=c2a945addf124caa9713f319622c43c4&st=1681722802716&sign=5d378de32665d9699581abce2a71a981&sv=102"

        response = get(url=url, headers=headers)
        data = response.json()
        token = data['token']

        headers = {
            'Host': 'lzkj-isv.isvjd.com',
            'User-Agent': UA,
            'Referer': 'https://lzkj-isv.isvjd.com/',
            'Cookie': cookies,
        }

        url = "https://lzkj-isv.isvjd.com/common/saveWqToken2?token={}&url=https://lzkj-isv.isvjd.com/wxAssemblePage/activity/67dfd244aacb438893a73a03785a48c7?activityId=67dfd244aacb438893a73a03785a48c7&adsource=tg_qrCode".format(token)

        response = get(url=url, headers=headers)

        url = "https://lzkj-isv.isvjd.com/customer/getMyPing"
        headers = {
            'Host': 'lzkj-isv.isvjd.com',
            'User-Agent':UA,
            'Origin': 'https://lzkj-isv.isvjd.com',
            'Referer':'https://lzkj-isv.isvjd.com/wxAssemblePage/activity/67dfd244aacb438893a73a03785a48c7?activityId=67dfd244aacb438893a73a03785a48c7&adsource=tg_qrCode',
            'content-type': 'application/x-www-form-urlencoded'
        }
        cookie = {
            'LZ_TOKEN_KEY': LZ_TOKEN_KEY,
            'LZ_TOKEN_VALUE': LZ_TOKEN_VALUE,
            'pt_pin': pt_pin,
            'pt_key': re.findall(r"pt_key=(.*?);", i)[0],
            'JSESSIONID': JSESSIONID
        }
        data = {
            'userId': '739130',
            'token': token,
            'fromType': 'APP',
        }

        response = post(url=url, headers=headers, data=data, _cookies=cookie)

        # data = response.json()
        # 将LZ_TOKEN_KEY，LZ_TOKEN_VALUE，AUTH_C_USER写入文件
        with open('./config/User_{}.json'.format(pt_pin), 'w',encoding='utf-8') as f:
            data = {
                'LZ_TOKEN_KEY': LZ_TOKEN_KEY,
                'LZ_TOKEN_VALUE': LZ_TOKEN_VALUE,
                'AUTH_C_USER': AUTH_C_USER
            }
            json.dump(data, f)
            f.close()
        # print(response.text)

        # print(data)
        # LZ_TOKEN_KEY = data['LZ_TOKEN_KEY']
        return True
    except:
        print('获取token失败')
        return False

async def sacn(bot,group_id,cookies,pt_pin):
    global LZ_AES_PIN
    global LZ_TOKEN_KEY
    global LZ_TOKEN_VALUE
    global JSESSIONID
    global AUTH_C_USER
    for num in range(1,nummax):
        # 如果是第4个和第5个，跳过
        if num == 4 or num == 5 or num == 6:
            continue
        for topNewType in range(1,3):
            flag_not_finish = True

            # 判读是否有./config/User_{}.json文件，如果有则读取，没有则getIsvToken
            if not os.path.exists('./config/User_{}.json'.format(pt_pin)):
                if (not init_User(cookies,pt_pin)):
                    return

            try:
                with open('./config/User_{}.json'.format(pt_pin), 'r',encoding='utf-8') as f:
                    data = json.load(f)
                    LZ_TOKEN_KEY = data['LZ_TOKEN_KEY']
                    LZ_TOKEN_VALUE = data['LZ_TOKEN_VALUE']
                    AUTH_C_USER = data['AUTH_C_USER']
                    f.close()
            except:
                print('读取文件失败')
                if (not init_User(cookies,pt_pin)):
                    return

            while (flag_not_finish):
                try:
                    headers = {
                        'Host': 'lzkj-isv.isvjcloud.com',
                        'Connection': 'keep-alive',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'X-Requested-With': 'XMLHttpRequest',
                        'User-Agent': UA,
                        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                        'Origin':'https://lzkj-isv.isvjcloud.com',
                        'Sec-Fetch-Site':'same-origin',
                        'Sec-Fetch-Mode':'cors',
                        'Sec-Fetch-Dest':'empty',
                        'Referer':'https://lzkj-isv.isvjcloud.com/wxAssemblePage/activity/?activityId=67dfd244aacb438893a73a03785a48c7&ID=0935160f681f4e9ca12d4a0780917a92',
                        'Accept-Encoding':'gzip, deflate',
                        'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                        'Cookie':"AUTH_C_USER={}; LZ_TOKEN_KEY={}; LZ_TOKEN_VALUE={};".format(AUTH_C_USER, LZ_TOKEN_KEY, LZ_TOKEN_VALUE)
                    }

                    data = {
                        'aggrateActType': num,
                        'topNewType': topNewType,
                        'pageNo': '1',
                        'pageSize': '100',
                        'pin': '{}'.format(AUTH_C_USER),
                    }

                    response = post('https://lzkj-isv.isvjcloud.com/wxAssemblePage/getTopAndNewActInfo', headers=headers, data=data)

                    data = json.loads(response.text)

                    active = data['data']['homeInfoResultVOList']

                    # print (active)
                    times = 0
                    for i in active:
                        # 获取activityId
                        activityId = i['activityId']
                        flag = True

                        # 判断activityId是否在文件中，如果在文件中，则跳过大循环，没有文件则创建
                        if not os.path.exists(PATH + '/data/scan_{}.txt'.format(num)):
                            with open(PATH + '/data/scan_{}.txt'.format(num), 'a') as f:
                                f.close()
                        with open(PATH + '/data/scan_{}.txt'.format(num), 'r') as f:
                            for line in f:
                                if activityId in line:
                                    flag = False
                        if flag:
                            # 如果不在文件中，则写入文件
                            with open(PATH + '/data/scan_{}.txt'.format(num), 'a') as f:
                                # str1 = "export M_WX_FOLLOW_DRAW_URL=\""  + i['activityUrl'] + "\""
                                str1 = i['activityUrl']
                                print(str1)
                                # if times == 5:
                                #     time.sleep(100)
                                #     times = 0
                                # times += 1
                                try:
                                    await bot.send_message(group_id,str1)
                                    f.write(activityId + '\n')
                                    time.sleep(30)
                                except:
                                    print("发送失败,try again")
                                    time.sleep(3)
                                    try:
                                        await bot.send_message(group_id,str1)
                                        f.write(activityId + '\n')
                                        time.sleep(30)
                                    except:
                                        print("发送失败, stop")

                                

                    print("scan_{}_{} 运行结束".format(num,topNewType))
                    flag_not_finish = False
                except:
                    print ("LZ_Token过期 尝试重新获取")
                    url = "https://lzkj-isv.isvjcloud.com/wxCommonInfo/token"
                    headers = {
                        'Host': 'lzkj-isv.isvjcloud.com',
                        'Connection':'keep-alive',
                        'accept': 'application/json, text/javascript, */*; q=0.01',
                        'user-agent': UA,
                        'accept-language': 'zh-Hans-JP;q=1, en-JP;q=0.9, zh-Hant-TW;q=0.8, ja-JP;q=0.7, en-US;q=0.6',
                        'X-Requested-With': 'XMLHttpRequest',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-Dest': 'empty',
                        'Cookie': "AUTH_C_USER={}; LZ_TOKEN_KEY={}; LZ_TOKEN_VALUE={};".format(AUTH_C_USER, LZ_TOKEN_KEY, LZ_TOKEN_VALUE),
                    }

                    body={}

                    response = post(url, headers=headers, data=body)

                    data = json.loads(response.text)
                    # LZ_TOKEN_KEY = data['data']['LZ_TOKEN_KEY']
                    # LZ_TOKEN_VALUE = data['data']['LZ_TOKEN_VALUE']

                    # 修改./config/User.json中的LZ_TOKEN_KEY,LZ_TOKEN_VALUE
                    with open('./config/User_{}.json'.format(pt_pin), 'r',encoding='utf-8') as f:
                        data = json.load(f)
                        data['LZ_TOKEN_KEY'] = LZ_TOKEN_KEY
                        data['LZ_TOKEN_VALUE'] = LZ_TOKEN_VALUE
                        with open('./config/User_{}.json'.format(pt_pin), 'w',encoding='utf-8') as f:
                            json.dump(data, f)
        # time.sleep(5)


if __name__ == '__main__':
    from jdCookie import get_cookies
    getCk = get_cookies()
    try:
        for i in getCk:
            LZ_TOKEN_KEY = ''
            LZ_TOKEN_VALUE = ''
            AUTH_C_USER = ''
            LZ_AES_PIN = ''
            JSESSIONID = ''
            pt_pin = re.findall(r"pt_pin=(.*?);", i)[0]
            asyncio.run(sacn(bot,group_id,i,pt_pin))
    except Exception as e:
        print(e)

