import requests  
from lxml import html  
import urlparse  
import collections

STARTING_URL = 'http://nytimes.com'

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
    saveFile = open("Titles.txt", "a")
    saveFile.write(str(printed) + '\n')

    # Find all links
    links = {urlparse.urljoin(response.url, url) for url in parsed_body.xpath('//a/@href') if urlparse.urljoin(response.url, url).startswith('http')}

    # Set difference to find new URLs
    for link in (links - found_urls):
        found_urls.add(link)
        urls_queue.append(link)
        #print link
        saveFile_Links = open("Titles_And_Links.txt", "a")
        saveFile_Links.write(str(link) + '\n')

saveFile.close()
saveFile_Links.close()
