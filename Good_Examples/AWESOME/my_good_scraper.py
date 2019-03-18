from bs4 import BeautifulSoup
import urllib
import urlparse

def response(url):
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

def response_tag_href(url):
    urls = [url] #stack of urls to scrape
    visited = [url] #historical record of urls
    while len(urls) >0:
        try:
            htmltext = urllib.urlopen(urls[0]).read()
        except:
                print(urls[0])
        soup = BeautifulSoup(htmltext)
        urls.pop(0) #print len(urls)
        #print (soup.findAll('a', href=True))
        for tag in soup.findAll('a', href=True):
                tag['href'] = urlparse.urljoin(url,tag['href'])
                if url in tag['href'] and tag['href'] not in visited:
                        urls.append(tag['href'])
                        visited.append(tag['href']) # historical record, whereas above line is temporary stack or queue
                # print visited
                print tag['href']


if __name__=='__main__':
    #print response('http://nytimes.com')
    print response_tag_href('https://query.nytimes.com/search/sitesearch/#/drone+strikes/')
