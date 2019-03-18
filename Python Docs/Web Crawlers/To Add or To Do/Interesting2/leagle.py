import requests  
from lxml import html  
import urlparse  
import collections

STARTING_URL = 'http://leagle.com'

urls_queue = collections.deque()  
urls_queue.append(STARTING_URL)  
found_urls = set()  
found_urls.add(STARTING_URL)

while len(urls_queue):  
    url = urls_queue.popleft()

    response = requests.get(url)
    parsed_body = html.fromstring(response.content)

    # Prints the page title
    #print parsed_body.xpath('//title/text()')
    finaltext = parsed_body.xpath('//title/text()')
    saveFile = open ('leagle_findall.txt','a')
    saveFile.write(str(finaltext) + '\n')
    
    # Find all links
    links = {urlparse.urljoin(response.url, url) for url in parsed_body.xpath('//a/@href') if urlparse.urljoin(response.url, url).startswith('http')}
    print links
    print '\n\n\n'
    saveFile.write(str(links) + '\n\n\n')

    # Set difference to find new URLs
    for link in (links - found_urls):
        found_urls.add(link)
        urls_queue.append(link)

    saveFile.close()
