import requests
import urllib
from lxml import html  
import urlparse  
import collections
import time

STARTING_URL = 'http://nytimes.com/pages/technology'

urls_queue = collections.deque()  
urls_queue.append(STARTING_URL)  
found_urls = set()  
found_urls.add(STARTING_URL)
links = set()

while len(urls_queue):
    try:

        url = urls_queue.popleft()
        request = urllib.urlopen(url)
        response = request.read()
    except:
        pass
    
    start = response.find("href=");
    while(start!=-1):
        end = response[start:].find(">");
        links = response[start+5:start+end]
        page = response[start+end:]
        found_urls.add(links)
        start = response.find("href=", start+1);

    # Find all links
    links_list = {urlparse.urljoin(response.url, url) for url in links if urlparse.urljoin(response.url, url).startswith('http')}
    #links = {links.add(link)}



    # Set difference to find new URLs
    for link in (links_list - found_urls):
        found_urls.add(link)
        urls_queue.append(link)
        print link
        saveFile = open("List_of_URLs.txt", "a")
        saveFile.write(str(link)+ '\n')
        saveFile.close()
