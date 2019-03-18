import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url = 'http://nytimes.com'
##base = 'http://nytimes.com'
##
##htmlfile = urllib.urlopen(url)
##
##soup = BeautifulSoup(htmlfile)
##
##for tag in soup.findAll('a',href=True):
##    print base + "/" + tag['href']
    
br = mechanize.Browser()

br.open(url)

for link in br.links():
##    print "The base URL is:" + link.base_url
##    print "The base URL is:" + link.url
    newurl = urlparse.urljoin(link.base_url, link.url)
    print link.text, '\n', newurl, '\n\n\n'
    
'''
htmlfile = urllib.urlopen(url)
soup = BeautifulSoup(htmlfile)
for tag in soup.findAll('a',href=True):
    print tag
''
