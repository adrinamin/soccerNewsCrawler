"""this is only a random crawler which provides information about soccer news.
Only for testing purposes.
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
from http.client import IncompleteRead


def getLigaInsiderNews():
    url = "https://www.ligainsider.de/"
    news = []
    n = []
    try:
        page = urlopen(url).read()
    except (IncompleteRead) as e:
        page = e.partial
    soup = BeautifulSoup(page,"lxml")
    for tag in soup.findAll("a",attrs={"profile_link_box", "newsboxlink"}):
        for child in tag.children:
            print(child.contents[0])
            if tag["class"] == ['newsboxlink']:
                print("https://www.ligainsider.de"+tag["href"])
            

def getBundesligeNews():
    url = "https://www.newsnow.co.uk/h/Sport/Football/Bundesliga?type=ln"
    try:
        page = urlopen(url).read()
    except (IncompleteRead) as e:
        page = e.partial
    soup = BeautifulSoup(page,"lxml")
    for tag in soup.findAll("div",attrs={"js-newsmain"}):
        children = tag.findChildren("a", attrs={"hll"})
        for child in children:
            print(child.contents[0])
            print(child["href"])

if __name__ == "__main__":
    getLigaInsiderNews()
    getBundesligeNews()