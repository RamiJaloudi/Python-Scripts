import mechanize
import urllib
from bs4 import BeautifulSoup
import urlparse

# url = 'http://www.leagle.com/featured-decisions'
# In the above URL, the title of the link is "read more" instead of the case name.
url = 'http://nytimes.com'

def is_there_law():
    br = mechanize.Browser()
    fd = br.open(url)
    return 'law' in fd.read().lower()

def find_links():
    br = mechanize.Browser()
    response = br.open(url)
    for link in br.links():
        print link.text,'\n', link.url, '\n\n\n'
        # this gives me the title of the url & the url itself. 

def Souper():
    htmlfile = urllib.urlopen(url)
    soup = BeautifulSoup(htmlfile)
    print soup.title
    for tag in soup.findAll('a',href=True):
        # print tag #here, it would also include the tag
   
        print tag['href']
        print urlparse.urlparse(tag['href']).hostname
        print urlparse.urlparse(tag['href']).path
        print '\n\n\n'

def Mechanizer_Sup():
    br = mechanize.Browser()
    urls = [url]
    visited = [url]
    try:
        while len(urls)>0:
            br.open(urls[0])
            urls.pop(0)
            with open("links.csv", "a") as file:
                for link in br.links():
                    newurl = urlparse.urljoin(link.base_url,link.url)
                    b1 = urlparse.urlparse(newurl).hostname
                    b2 = urlparse.urlparse(newurl).path
                    newurl = "http://" + b1 + b2
                    print newurl
                    file.write(newurl + "\n")
                    
                if newurl not in visited and urlparse.urlparse(url).hostname not in newurl:
                    visited.append(newurl)
                    urls.append(newurl)
                    print newurl
                    #file.write(newurl + "\n\n")
                 
    except:
        print "error"
        urls.pop(0)
            
            

if __name__ == '__main__':
    if is_there_law():
        print 'Yes!'
    else:
        print 'No!'
    #find_links()
    #Souper()
    Mechanizer_Sup()
    
 
