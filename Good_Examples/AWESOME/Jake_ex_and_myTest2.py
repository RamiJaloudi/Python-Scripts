import requests
import urllib
from lxml import html  
import urlparse  
import collections
import time

STARTING_URL = 'http://nytimes.com/pages/technology'
urls_queue = set()
urls_queue = collections.deque()  
urls_queue.add(STARTING_URL)  
found_urls = set()  
found_urls.add(STARTING_URL)

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
        link = response[start+5:start+end]
        page = response[start+end:]
        found_urls.add(link)
        #links.add(link)
        #print(link)
        start = response.find("href=", start+1);
        #time.sleep(5)

    #Prints the page title
    #print parsed_body.xpath('//title/text()')
    #print link

    # Find all links
    #links = {urlparse.urljoin(response.url, url) for url in link if urlparse.urljoin(response.url, url).startswith('http')}

    # Set difference to find new URLs
    for link in found_urls:
        #found_urls.add(link)
        urls_queue.add(link)
        #print link
print found_urls
saveFile = open("List_of_URLs.txt", "a")
saveFile.write(str(found_urls)+ '\n')
saveFile.close()
