import requests
import re
import json
import time
from requests.exceptions import RequestException

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36(KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537/36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile(
    '<dd>.*?board-index.*?>(.*?)</i>.*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?</i>.8?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield{
            'index':item[0],
            'title':item[1],
            'actor':item[2].strip()[3:],
            'time':item[3].strip()[5:],
            'score':item[4] + item[5]
        }
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dump(content, ensure_ascii=False) + '\n')

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__=='__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)