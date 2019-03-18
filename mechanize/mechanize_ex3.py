import urllib, urlparse, mechanize

from bs4 import BeautifulSoup

url = 'http://nytimes.com'

br = mechanize.Browser()
br.open(url)
for link in br.links():
    newurl = urlparse.urljoin(link.base_url,link.url)
    b1 = urlparse.urlparse(newurl).hostname
    b2 = urlparse.urlparse(newurl).path
    alt_newurl = "http://" + b1 + b2
    print alt_newurl
