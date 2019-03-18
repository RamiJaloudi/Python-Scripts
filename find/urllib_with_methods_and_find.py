import urllib

# This script runs on Python 2.7
# If using Python 3, please note that the urllib module has been split into parts and renamed as follows:
# urllib.request, urllib.parse, and urllib.error

url = "http://www.nytimes.com" # Need to enter URL

request = urllib.urlopen(url)
page = request.read()
#print response

def getTitle(page): # extract Title of page
        start = page.find("<title>");
        end = page.find("</title>");
        titleText1 = page[start+7:end]
        titleText2 = page[start:end+8]
        print titleText1
        print titleText2

def extractAnchor(page): # extract all hyperlinks on the page
    links = [ ]
    index = page.find('<a')
    while index != -1:
        inx2 = page.find('</a>',index)
        links.append(page[index:inx2+4])
        index = page.find('<a', index+1)
    print(len(links), 'links in page\n') # number of links in page
    for link in links:
        print(link)

def extractLinks(page): # extract all links in the page
    start = page.find("href=");
    while(start!=-1):
        end = page[start:].find(">");
        link = page[start+5:start+end]
        page = page[start+end:]
        print(link)
        start = page.find("href=");

def extractAllPars(page): # extract all hyperlinks on the page
    allpars = [ ]
    pars = page.find("<p>");
    while pars != -1:
        pars2 = page.find('</p>',pars)
        allpars.append(page[pars:pars2+4])
        pars = page.find('<p>', pars+1)
    print(len(allpars), '<p> tags in page\n') # number of <p< tags in page
    for par in allpars:
        print(par)

##getTitle(page)
extractAnchor(page)
##extractLinks(page)
##extractAllPars(page)
