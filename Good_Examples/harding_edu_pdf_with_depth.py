import urllib
from bs4 import BeautifulSoup
import urlparse
import time


start = "http://wikipedia.com", "http://yahoo.com", "http://google.com"

def crawl(seeds):

    frontier = seeds
##    visited_urls = set()
    visited_urls = set()

    with open("links.csv", "a") as file:

        for crawl_url in frontier:
          
            print "Crawling:", crawl_url
            #ornvisited_urls.append(crawl_url)
            print type(frontier)
           

            try:
                c = urllib.urlopen(crawl_url)
            except:
                print "Could not access", crawl_url
                continue

            content_type = c.info().get('Content-Type')
            if not content_type.startswith('text/html'):
                continue

            soup = BeautifulSoup(c.read())
            discovered_urls = set()
            links = soup('a') # Get all anchor tags
            for link in links:
                if('href' in dict(link.attrs)):
                    url = urlparse.urljoin(crawl_url, link['href'])
                    #url = urljoin(crawl_url, link['href'])
                    if(url[0:4] == 'http' and url not in visited_urls
                       and url not in discovered_urls and url not in frontier):
                        discovered_urls.add(url)
         
                        
##            frontier = frontier, discovered_urls
####            repr_frontier = repr(frontier)
####            repr_discovered_urls = repr(discovered_urls)
##            list_frontier = list(frontier)
##            print type(discovered_urls)

            frontier = frontier, discovered_urls
            strings = str(frontier)
           
            file.write(str(strings) + '\n')
        
            #print discovered_urls
            time.sleep(2)
            #file.write(str(frontier) + '\n')

crawl(start)
