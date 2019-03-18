import urllib
from bs4 import BeautifulSoup

url = "http://nytimes.com"

request = urllib.urlopen(url)
print request

#soup = BeautifulSoup(response)


