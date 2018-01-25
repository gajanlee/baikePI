from core import *
from core.base import *

class BaiduBaike(Pedia):
    def item_url(self, word):
        self.word = word
        return "http://baike.baidu.com/item/" + word

    def get_multi_sense(self):
        senses = []
        for item in self.content_soup.find_all(class_="item"):
            if item.a is not None:
                senses.append((item.a.get('href'), item.a.string))
            else:
                select = item.span.string
        return select, senses

    def get_attr(self):
        attrs = {}
        items = self.content_soup.find_all(attrs={'class': re.compile('basicInfo-item')})
        for i in range(0, len(items), 2):
            attrs[items[i].string] = items[i+1].text
        return attrs

    def get_summary(self):
        return self.content_soup.find(attrs={'class': 'lemma-summary'}).text

    def notFound(self):
        if self.content_soup.find("sorryTxt") is not None:
            return False
        return True

    def __repr__(self):
        return r'BaiduBaike("%s")' % self.word

if __name__ == "__main__":
    print(BaiduBaike("周杰伦X").get_summary())