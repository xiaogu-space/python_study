# coding:utf-8
# by NeilShi 11/29/2017
import requests
import hashlib
import base64
import json
import os

# 'appkey': '154430',
# 'AppSecret': 'S7ib51Kp5......Qd10Lt4490QTwpr',
# 资源：d0119848ab5......df5d8d6dc149

url = 'http://link.cainiao.com/gateway/link.do'
keys = '746gN2658u...G18TK99v4'

headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}

results = ''  # 存放结果集


def get_address():
    try:
        with open(os.getcwd() + r'/address.txt', 'r') as f:
            address = f.readlines()
        return address
    except:
        print('打开文件失败')
        return ''


def get_raw_input(address):
    raw_input = {"address": address, "limit": "2"}
    return raw_input


def get_param(sign, content):
    param = {
        'msg_type': 'CNDZK_ADDRESS_QUERY',
        'data_digest': sign,
        'logistic_provider_id': '1f04f09eb...303e553924',
        'logistics_interface': content
    }
    return param


def get_data_digest(inputs, keys):
    m1 = hashlib.md5()
    m1.update((inputs + keys).encode('utf-8'))

    # base64.b64encode(m1.hexdigest()) 得到错误值!!!原因未知
    return base64.b64encode(m1.digest())


address_list = get_address()

for x in address_list:
    # unicode形态转中文，去掉空格（否则查不出）
    inputs = json.dumps(
        get_raw_input("北京朝阳区西大望路甲12号国家广告产业园A座")).encode('utf-8').decode('unicode_escape').replace(
            ' ', '')
    dataGet=get_param(get_data_digest(inputs, keys), inputs)
    result = requests.post(
        url,
        data=dataGet,
        headers=headers)
    result = result.content.decode(encoding='utf-8')
    # print(result)
    results = results + result + '\r\n'

try:
    with open(os.getcwd() + r'/result.txt', 'w') as f:
        f.write(results)
        print("写入成功")
except:
    print("写文件失败")