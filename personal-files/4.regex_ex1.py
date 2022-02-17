    
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
""" images = bs.findAll('img',
{'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')}) """
images = bs.findAll('img',
{'src':re.compile('^\.\.\/(img){1}\/(gifts){1}\/(img){1}.*\.(jpg){1}$')})
for image in images:
    print(image['src'])

# print(images)


