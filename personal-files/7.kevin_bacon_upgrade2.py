    
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(None)

def getLinks(articleUrl):
        html = urlopen(articleUrl)
        bs = BeautifulSoup(html, 'html.parser')
        return bs.find('div', {'id':'bodyContent'}).findAll('a', {'href': re.compile('^(/wiki/)((?!:).)*$')})

links = getLinks('http://en.wikipedia.org/wiki/Kevin_Bacon')
counter = 1
while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        links = getLinks('http://en.wikipedia.org' + newArticle)
        



