#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 2:00
# @Belongs  : InteIJ群管理者所有
# @File    : jdCookie.py
# @Reason : 适应群内项目
# @Revise : 适配代理和活动项目的个人定制版本
"""
添加代理变量 JK_ALL_PROXY
export JK_ALL_PROXY="http://IP:端口";

定时任务 BAN_TIMING
export BAN_TIMING="0&1&2";
时间0-23 别问问为什么没有24

脚本黑白名单 PASS_SCRIPT
export PASS_SCRIPT="jd_fruit_task.js&jd_wsdlb.js";
如果代理使用白名单，就把65行删了, 如果使用黑名单就把54 行删了或者前面加 # ，默认添加都走代理
os.environ['ALL_PROXY'] = JK_ALL_PROXY

专门适配活动参数的
export NOT_CJ="pt_pin1&pt_pin2" CJ开头黑名单
export NOT_LZ="pt_pin1&pt_pin2" LZ开头黑名单
"""

import os
import re
import sys
import time
from functools import partial

print = partial(print, flush=True)

PASS_SCRIPT = os.environ.get('PASS_SCRIPT', '')
JK_ALL_PROXY = os.environ.get('JK_ALL_PROXY', None)
BAN_TIMING = os.environ.get('BAN_TIMING', '')
NOT_TYPE = os.environ.get('NOT_TYPE', None)

NOT_CJ = []
NOT_LZ = []

hours_ti = time.localtime().tm_hour

# 定时任务,默认填写的为黑名单时间
if hours_ti in BAN_TIMING.split('&'):
    print(f'检测到 {hours_ti} 时在 BAN_TIMING 变量中执行此输出')
else:
    # 代理获取执行脚本名称的
    PASS_SCRIPT = os.environ.get('PASS_SCRIPT', '')
    # 检测脚本在不在黑白名单
    if re.findall('(\w+\.py)', sys.argv[0])[0] in PASS_SCRIPT.split("&"):
        print("这里可以填写代理 PASS_SCRIPT为白名单")
        # 下面是代理可以删除
        # os.environ['IP_ALL_PROXY'] = JK_ALL_PROXY
    elif NOT_TYPE:
        # 这里是活动的，如果你只是使用代理而没有使用活动请勿修改
        NOT_CJ = os.environ.get('NOT_CJ', '').split('&')
        NOT_LZ = os.environ.get('NOT_LZ', '').split('&')
        print('检测到活动类型执行')
        # 下面是代理可以删除
        os.environ['IP_ALL_PROXY'] = JK_ALL_PROXY
    else:
        print("这里也可以填写代理 PASS_SCRIPT 为黑名单")
        # 下面是代理可以删除
        # os.environ['IP_ALL_PROXY'] = JK_ALL_PROXY


def ck_detection(JD_COOKIE: list):
    """
    检测CK黑名单中不
    :param JD_COOKIE:
    :return:
    """
    JD_CK = []
    for JD in JD_COOKIE:
        j_ck = re.findall('pt_pin=(\w+);', JD)
        if NOT_TYPE == 'cj' and j_ck in NOT_CJ:
            continue
        elif NOT_TYPE == 'lz' and j_ck in NOT_LZ:
            continue
        else:
            JD_CK.append(JD)
    return JD_CK


def get_cookies():
    CookieJDs = []
    if os.environ.get("JD_COOKIE"):
        print("已获取并使用Env环境 Cookie")
        if '&' in os.environ["JD_COOKIE"]:
            CookieJDs = ck_detection(os.environ["JD_COOKIE"].split('&'))
        elif '\n' in os.environ["JD_COOKIE"]:
            CookieJDs = ck_detection(os.environ["JD_COOKIE"].split('\n'))
        else:
            CookieJDs = [os.environ["JD_COOKIE"]]
        # return CookieJDs
    else:
        if os.path.exists("JD_COOKIE.txt"):
            with open("JD_COOKIE.txt", 'r') as f:
                JD_COOKIEs = f.read().strip()
                if JD_COOKIEs:
                    if '&' in JD_COOKIEs:
                        CookieJDs = ck_detection(JD_COOKIEs.split('&'))
                    elif '\n' in JD_COOKIEs:
                        CookieJDs = ck_detection(JD_COOKIEs.split('\n'))
                    else:
                        CookieJDs = [JD_COOKIEs]
                    CookieJDs = sorted(set(CookieJDs), key=CookieJDs.index)
                    # return CookieJDs
        else:
            print("未获取到正确✅格式的京东账号Cookie")
            return

    print(f"====================共{len(CookieJDs)}个京东账号Cookie=========\n")
    print(
        f"==================脚本执行- 北京时间(UTC+8)：{time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())}=====================\n")
    return CookieJDs


if __name__ == "__main__":
    get_cookies()
    print(os.environ.get("JD_COOKIE"))
