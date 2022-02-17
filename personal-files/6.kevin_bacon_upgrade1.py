    
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
bodyContentDiv = bs.find('div', {'id':'bodyContent'})
anchors = bodyContentDiv.findAll('a', {'href': re.compile('^(/wiki/)((?!:).)*$')})
for link in anchors:
        print(link['href'])



