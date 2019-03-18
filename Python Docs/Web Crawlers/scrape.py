# Python_Page_Spider_Web_Crawler_Tutorial
# from https://www.youtube.com/watch?v=SFas42HBtMg&list=PLa1r6wjZwq-Bc6FFb9roP7AZgzDzIeI8D&index=3
# Spider algorithm.
# You need to EXECUTE the file in Shell, e.g.  execfile("nytimes/scrape.py")

import urlparse
import urllib
#import urllib.request for Python3?
from bs4 import BeautifulSoup

url = "http://nytimes.com"
urls = [url] #stack of urls to scrape
visited = [url] #historical record of urls

while len(urls) >0:
        try:
                htmltext = urllib.urlopen(urls[0]).read()
        except:
                print(urls[0])
        soup = BeautifulSoup(htmltext)
        urls.pop(0) #print len(urls)
        print (soup.findAll('a', href=True))

        for tag in soup.findAll('a', href=True):
                tag['href'] = urlparse.urljoin(url,tag['href'])
                if url in tag['href'] and tag['href'] not in visited:
                        urls.append(tag['href'])
                        visited.append(tag['href']) # historical record, whereas above line is temporary stack or queue
                print visited	
	
		
	
