# coding:utf-8

import requests
import re

from requests.exceptions import RequestException
from multiprocessing import Pool


headers = {'User-Agent': 'Mozilela/5.0 '}

# 构造下载器
def get_one_page(url):
    try:
        res = requests.get(url, headers = headers)
        if res.status_code == 200:
            return res.text
        else:
            return None

    except RequestException:
        return None

# 构造html解析器
def parse_one_page(html):
    regex = """
    <dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a
    .*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>
    .*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S
    """
    pattern = re.compile(regex)
    items = re.findall(pattern, html)

    for item in items:
        yield {
            'index': items[0],
            'image': items[1],
            'title': items[2],
            'actor': items[3].strip()[3:],
            'time': items[4].strip()[5:],
            'score': items[5] + items[6]
        }


# 构造数据存储器
def write_to_file(content):
    with open('result.txt', 'a', encoding = 'utf-8') as file:
        file.write(json.dumps(content, ensure_ascii = False) + '\n')
        file.close()


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print item
        write_to_file(item)

if __name__ == '__main__':
    p = Pool()
    p.map(main, [i * 10 for i in range(10)])



