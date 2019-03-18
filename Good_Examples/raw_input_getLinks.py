import urllib
import re

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()

links = re.findall('href="(http://.*?)"', html)

x = 0

for link in links:
    x = x + 1
    print link

print x
    
