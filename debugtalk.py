import json
import time

import requests
from httprunner import __version__
from common.baseapi import BaseApi
from common.login import Login

"""
动态运算文件
自定义方法
"""

def get_httprunner_version():
    return "httprunner"+__version__


def sleep(n_secs):
    time.sleep(n_secs)

# todo 获取通用账号token
def get_token():
    return Login().login()

# todo 获取通用headers
def get_headers():
    return {"accept": "application/json, text/plain, */*",
            "content-type": "application/json;charset=UTF-8",
            "authorization": "Bearer ${get_token()}",
            "user-agent": "${get_httprunner_version()}",}


# todo 获取特殊token单独处理
def get_admin_token():

    data={
            "method": "POST",
            "url": "https://xxx.xxx.cn/api/login/",
            "json": {"email":"xxx","password":"xxx"}
        }

    res = BaseApi.http_api(data)
    admin_token = res.json()
    return admin_token["data"]["token"]
