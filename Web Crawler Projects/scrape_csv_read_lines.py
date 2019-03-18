# Python_Page_Spider_Web_Crawler_Tutorial
# from https://www.youtube.com/watch?v=SFas42HBtMg&list=PLa1r6wjZwq-Bc6FFb9roP7AZgzDzIeI8D&index=3
# Spider algorithm.
# You need to EXECUTE the file in Shell, e.g.  execfile("nytimes/scrape.py")
# First open cmd.  Then cd C:\Users\Joh\Documents\Python Scripts\Web Crawler Projects\nytimes.
# Then enter Python Scrape.py

import urllib.parse
import urllib
#import requests
from bs4 import BeautifulSoup
import csv

r = csv.reader(open("top500.domains.01.14.csv"))
#line1=r.next()
#line2=r.next()

url_queue
for row in r:
        url_queue.append(row[2])
        
url = url_queue
# url = line1=r.next()
# url = "http://news.google.com, http://nytimes.com"
urls = [url] #stack of urls to scrape
visited = [url] #historical record of urls

while len(urls) >0:
        try:
                htmltext=urllib.request.urlopen(url[0])
                #htmltext = requests.get(urls)
        except:
                print (urls[0])

        soup = BeautifulSoup(htmltext)

'''
while len(urls) >0:
        try:
                htmltext = urllib.urlopen(urls[0]).read()
        except:
                print urls[0]

        soup = BeautifulSoup(htmltext)

        urls.pop(0)
        # print len(urls)
        # print soup.findAll('a', href=True)
        items = soup.findAll('a', href=True)
        saveFile = open ('crawl_findall.txt','w')
        saveFile.write(str(items))
        saveFile.close()
        print items

        for tag in soup.findAll('a', href=True):
                # print tag
                # print tag['href'] # is you just want to print href
                tag['href'] = urlparse.urljoin(url,tag['href'])
                #print tag['href']
                if url in tag['href'] and tag['href'] not in visited:
                        urls.append(tag['href'])
                        visited.append(tag['href']) # historical record, whereas above line is temporary stack or queue.
                print visited	
'''
