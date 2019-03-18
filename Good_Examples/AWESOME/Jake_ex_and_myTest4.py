import requests  
from lxml import html  
import urlparse  
import collections

import time


def MyCrawler():
    
    STARTING_URL = 'https://query.nytimes.com/search/sitesearch/#/drone+strikes/'

    urls_queue = collections.deque()  
    urls_queue.append(STARTING_URL)  
    found_urls = set()  
    found_urls.add(STARTING_URL)

    while len(urls_queue):
        try:
            
            url = urls_queue.popleft()

            response = requests.get(url)

        except:
            pass
        
        parsed_body = html.fromstring(response.content)
        

        # Prints the page title
        printed = parsed_body.xpath('//title/text()')
        print printed
        saveFile = open("Title.txt", "a")
        saveFile.write(str(printed) + '\n')

        # Find all links
        links = {urlparse.urljoin(response.url, url) for url in parsed_body.xpath('//a/@href') if urlparse.urljoin(response.url, url).startswith('http')}

        # Set difference to find new URLs
        for link in (links - found_urls):
            found_urls.add(link)
            urls_queue.append(link)

    saveFile.close()


t_end = time.time() + 10
while time.time() < t_end:
    MyCrawler()
