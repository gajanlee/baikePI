from core import *

class Pedia(ABC):
    def __init__(self, word):
        self.get_html(word)
        log("Start ..." + repr(self))

    def get_html(self, word):
        rep = requests.get(self.item_url(word), headers=headers)
        self.content_soup = BeautifulSoup(rep.content, "lxml")
        return self.notFound()

if __name__ == "__main__":
    print(headers)