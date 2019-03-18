from bs4 import BeautifulSoup
import urllib, urlparse, re

def response(url):
    urls = [url] #stack of urls to scrape
    visited = [url] #historical record of urls
    while len(urls) >0:
        try:
            htmltext = urllib.urlopen(urls[0])
            text = htmltext.read()
        except:
                print(urls[0])
        #soup = BeautifulSoup(htmltext)
        urls.pop(0) #print len(urls)
        #print (soup.findAll('a', href=True))
        pat1 = re.compile(r'<h3>.+?</h3>', re.I|re.M)
        title1 = re.findall(pat1, str(text))
        print title1
        print '\n\n\n'
        saveFile = open ('dronesNYTimes_findall.txt','a')
        saveFile.write(str(title1) + '\n\n\n')

        pat2 = re.compile(r'<h4></h4><p>.+?</p>', re.I|re.M)
        title2 = re.findall(pat2, str(text))
        print title2
        print '\n\n\n'
        saveFile = open ('droneNYTimes_findall.txt','a')
        saveFile.write(str(title2) + '\n\n\n')

##        pat3 = re.compile(r'<h4></h4><p>.+?</a>', re.I|re.M)
##        title3 = re.findall(pat3, str(text))
##        print title3
##        print '\n\n\n'
##        saveFile = open ('leagle_findall.txt','a')
##        saveFile.write(str(title3) + '\n\n\n')
##        
##        saveFile.close()
    


##def response_tag_href(url):
##    urls = [url] #stack of urls to scrape
##    visited = [url] #historical record of urls
##    while len(urls) >0:
##        try:
##            htmltext = urllib.urlopen(urls[0]).read()
##        except:
##                print(urls[0])
##        soup = BeautifulSoup(htmltext)
##        urls.pop(0) #print len(urls)
##        #print (soup.findAll('a', href=True))
##        for tag in soup.findAll('a', href=True):
##                tag['href'] = urlparse.urljoin(url,tag['href'])
##                if url in tag['href'] and tag['href'] not in visited:
##                        urls.append(tag['href'])
##                        visited.append(tag['href']) # historical record, whereas above line is temporary stack or queue
##                # print visited
##                print tag['href']


if __name__=='__main__':
    print response('http://nytimes.com')
    #print response_tag_href('http://leagle.com/decisions/latest/New%20Jersey')
