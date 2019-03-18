import urllib
from bs4 import BeautifulSoup

url = 'https://nytimes.com'

request = urllib.urlopen(url)
response = request.read()

soup = BeautifulSoup(response)

print soup.get_text()

