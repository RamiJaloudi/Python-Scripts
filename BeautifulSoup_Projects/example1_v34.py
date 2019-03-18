import requests
from bs4 import BeautifulSoup

r = requests.get("http://nytimes.com")
# print r.content  # this will print out the content. This is why BS comes in handy.

soup = BeautifulSoup(r.content)
# print soup.prettify() # Gives a slightly better format.
# s = soup.find_all("a")
# print s

for link in soup.find_all("a"):
    print link
    # link.get("href")
    # print link.get("href")
    # print link.text
