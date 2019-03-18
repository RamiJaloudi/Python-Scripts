#Christopher Reeves Web Scraping Tutorial
#getting page source with python
#http://youtube.com/creeveshft
#http://christopherreevesofficial.com
#http://twitter.com/cjreeves2011

import urllib
from bs4 import BeautifulSoup

url = "http://news.google.com"

htmltext = urllib.urlopen(url).read()
print htmltext

soup = BeautifulSoup(htmltext)
print soup

