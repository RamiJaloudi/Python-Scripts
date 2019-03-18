import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('a')

x = 0

for tag in tags:
    x = x + 1
    print tag.get('href', None)

print x 
    
