from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())
    """
    Here we are using get_text function.
    pay attention because when you use get_text all tags and hyperlinks
    will be stripped away so it's always better preserve 
    BeautifulSoup object structure, instead of get_text
    """ 

