from bs4 import BeautifulSoup
import urllib

url = 'http://nytimes.com'
html = urllib.urlopen(url)
r = html.read()
soup = BeautifulSoup(r)
links = soup('a')

print len(links)

print type(links)

