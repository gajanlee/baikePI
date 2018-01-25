import requests
from bs4 import BeautifulSoup
import re

def get_sense(word):
    headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Referer': 'http://www.zhihu.com/articles'
    }
    rep = requests.get("http://baike.baidu.com/item/" + word + "/22064858", headers=headers)
    soup = BeautifulSoup(rep.content)
    for i in soup.find_all(class_="item"):
        print(i.a.get('href') if i.a != None else i.span.string)

    dict = {}
    items = soup.find_all(attrs={'class': re.compile('basicInfo-item')})
    for i in range(0, len(items), 2):
        dict[items[i].string] = items[i+1].text
    print(dict)


if __name__ == "__main__":
    get_sense("稻香")