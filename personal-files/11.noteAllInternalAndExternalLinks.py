from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re

# Collects a list of all external URLs found on the site
allExtLinks = set()
allIntLinks = set()

#Retrieves a list of all Internal links found on a page
def getInternalLinks(bsObj, includeUrl):
    print ('link da INCLUDE {}'.format(includeUrl))
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []
    #Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks
            
#Retrieves a list of all external links found on a page
def getExternalLinks(bsObj, excludeUrl):
    print ('link da EXCLUDE {}'.format(excludeUrl))
    externalLinks = []
    #Finds all links that start with "http" or "www" that do
    #not contain the current URL
    for link in bsObj.findAll("a", href=re.compile(
                                "^(http|www|https)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getAllExternalLinks(siteUrl):
    # print('Url to open: {}'.format(siteUrl))
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme, urlparse(siteUrl).netloc)
    # print('Domain to incluse/exclude: {}'.format(domain))
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            # print('EXT added link: {}'.format(link))
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            # print('INT added link: {}'.format(link))
            getAllExternalLinks(link)

allIntLinks.add('http://oreilly.com')
getAllExternalLinks('http://oreilly.com')
    
