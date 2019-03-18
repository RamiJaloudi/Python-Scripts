
import requests
from bs4 import BeautifulSoup

url = "http://news.google.com"
urls = [url] #stack of urls to scrape
visited = [url] #historical record of urls

r = requests.get(url[0])

while len(urls) >0:
        try:
                soup = BeautifulSoup(r.content)
        except:
                print urls[0]

        
        #urls.pop(0)


