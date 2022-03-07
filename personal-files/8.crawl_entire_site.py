from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        # I added this second condition otherwise the script crwal the same link anytime
        if (('href' in link.attrs) and (link.attrs['href'] not in pages)): 
            #We have encountered a new page
            newPage = link.attrs['href']
            print(newPage)
            pages.add(newPage)
            getLinks(newPage)
getLinks('')