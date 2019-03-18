import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url = "http://www.library.fordham.edu/"
br = mechanize.Browser()
urls = [url]
visited = [urls]
while len(urls)>0:

    try:

        br.open(urls[0])
        #urls.pop(0)
        
        with open("links.csv", "w") as file:
            for link in br.links(0):
                newurl = urlparse.urljoin(link.base_url, link.url)
                b1 = urlparse.urlparse(newurl).hostname
                b2 = urlpase.urlparse(newurl).path
                newurl = "http://" + b1 + b2
                file.write(newurl + "\n")

            if link not in visited and urlpase.urlparse(url).hostname in newurl:
                urls.append(newurl)
                visited.append(newurl)
                file.write(newurl + "\n")

    except:
        print "error"
        urls.pop(0)
                

