# coding:utf-8

import requests
import re
import json

from requests.exceptions import RequestException
from multiprocessing import Pool

# 参考文章地址:
'''
https://mp.weixin.qq.com/s?__biz=MzA5MzY4NTQwMA==&mid=2651003388&idx=1&sn=d70ff361d83ee3d0ba14fa4a814721f4&chksm=8badaa0bbcda231d97f95fdae603c54da46b01e66dd438cf6914c404abf18caac5a91ac1a99b&mpshare=1&scene=23&srcid=0408LXS1WXKuKj18eKQVqnB2%23rd
'''

# 从Safari中获取的HTTP头
headers = {
    # 'Cookie': '__mta=214924840.1542867076545.1542867076545.1542867120165.2; _lxsdk_s=1673a0b40e2-878-423-26e%7C%7C16; __mta=248435256.1542867117003.1542867117003.1542867117003.1; _lxsdk=6A8E19C0EE1D11E893CBAD8587413DE9A22C7BABCAFB4C1787EE697E8A0470AE; _lxsdk_cuid=1673a0b40e1c8-04cc3474cf27128-481c3400-1aeaa0-1673a0b40e1c8; _csrf=bad4b01703d58f328190ae424763edbf8b378121a23fede8011990eda52f34a5; uuid=6A8E19C0EE1D11E893CBAD8587413DE9A22C7BABCAFB4C1787EE697E8A0470AE; uuid_n_v=v1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}


# 构造下载器
def get_one_page(url):
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        else:
            print('请求失败: code = %d, res = %r' % (res.status_code, res))
            return None

    except RequestException, value:
        print '请求异常日志:' + value
        return None


# 构造html解析器
def parse_one_page(html):
    regex = '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a' + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>' + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>'

    pattern = re.compile(regex, re.S)
    items = re.findall(pattern, html)

    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


# 构造数据存储器
def write_to_file(content):
    with open('MaoYan.txt', 'a') as file:
        json_str = json.dumps(content)
        # Unicode编码的中文先给转为中文, 然后再已utf-8的形式写入文件
        json_str = json_str.decode("unicode-escape").encode('utf-8')
        json_str += '\n'

        print('写入文件: %r' % json_str)
        file.write(json_str)
        file.close()


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    list = parse_one_page(html)

    print(html)
    print(list)
    for item in list:
        # print item
        write_to_file(item)


print(__name__)

if __name__ == '__main__':
    p = Pool()
    p.map(main, [i * 10 for i in range(10)])

with open('MaoYan.txt', 'r') as file:
    print 'file read>>>>>> ' + file.read()
    file.close()
