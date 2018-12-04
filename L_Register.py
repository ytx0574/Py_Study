# coding:utf-8




# https://api.tgceshi.com:6869/lottery-api/api/v2/user/register
# , Headers: {
#     "Accept-Language" = "en;q=1";
#     "Content-type" = "application/json; charset=UTF-8";
#     "User-Agent" = ios;
#     deviceId = "BDD2D49A-EA59-46AE-A6F7-F3562FDDE555";
#     deviceName = "iPhone XS Max (A1921/A2101/A2102/A2104)";
#     key = "e0uswxzKCML0ZXeIEqyWwZGP3pH0Knb9NWyBGu+NwuBN6PUogq1AC4M+AV1aEEJLmwW6+9mn3/ZkOPPGYZRbwXGP+b7jjZ6RkW+rjIYoip281tyT+y0qAe8yQXBkdnldaGFCRSF54/rbJUYrYTzca/OKPMi1K65v10wNbazZJZo=";
#     packageName = "com.ufun.lottery.test";
#     sign = d352d3a331849c55aa5a7775da0e80f9;
#     timestamp = 1543832085;
#     version = "1.5.0";
# }, Parameter: {
#     email = "";
#     expandCode = "";
#     idCard = "";
#     password = 343b1c4a3ea721b2d640fc8700db0f36;
#     phone = 15600000000;
#     qq = "";
#     realName = "";
#     userCode = Ytx8083;
#     userType = 00;
#     wechat = "";
# }

import requests
import json
import time
import hashlib
import random
import rsa
from requests.exceptions import RequestException


def stringWithBitLength(length):
    seed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(length):
        sa.append(random.choice(seed))

    return ''.join(sa)



hashlib_md5 = hashlib.md5()

timestamp = str(int(time.time()))
sign = timestamp + '##Lottery2017$$'
hashlib_md5.update(sign)
sign = hashlib_md5.hexdigest()


rsa
merchant_aes_key = 'QJQJEMDMONXTDXKH'
rsa_public_key = """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCRQZ5O/AOAjeYAaSFf6Rjhqovws78I716I9oGF7WxCIPmcaUa1Yuy
LOncCCuPsaw69+RMWjdbOBp8hd4PPM/d4mKTOVEYUE0SfxhhDTZaM5CzQEUXUyXy7icQTGR5wBjrbjU1yHCKOf5
PJJZZQWB06husSFZ40TdL7FdlBpZ1u1QIDAQAB
-----END PUBLIC KEY-----
"""

aes_key = rsa.encrypt(merchant_aes_key.encode(), rsa.PublicKey.load_pkcs1(open('/Users/johnson/Desktop/cacert.pem').read()))


headers = {
    'Content-type': "application/json; charset=UTF-8",
    'User-Agent': 'ios',
    'deviceId': 'BDD2D49A-EA59-46AE-A6F7-F3562FDDE555',
    'deviceName': 'iPhone XS Max (A1921/A2101/A2102/A2104)',
    # 'key': '++/+++//=',
    'packageName': 'com.ufun.lottery.test',
    'sign': sign,
    'timestamp': timestamp,
    'version': '1.5.0'
}

parametters = {
    'email': '',
    'expandCode': '',
    'idCard': '',
    'password': '343b1c4a3ea721b2d640fc8700db0f36',
    'phone': '',
    'qq': '',
    'realName': '',
    'userCode': 'ytxx8081',
    'userType': '00',
    'wechat': '',
}

try:
    request = requests.post('https://api.tgceshi.com:6869/lottery-api/api/v2/user/register', headers=headers, json=json.dumps(parametters))
    if request.status_code == 200:
        print request.content
        pass
    else:
        pass

except RequestException, value:
    print '请求异常日志:' + value