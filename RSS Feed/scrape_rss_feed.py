import urllib
import urllib2
import re
import cookielib
from cookielib import CookieJar
import time

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def main():
    try:
        page = 'http://feeds.reuters.com/reuters/topNews'
        sourceCode = opener.open(page).read()
        #print sourceCode

        try:
            titles = re.findall(r'<title>(.*?)</title>', sourceCode)
            #links = re.findall(r'<link.*?href="(.*?)"', sourceCode)
            links = re.findall(r'<link>(.*?)</link>', sourceCode)
##            for title in titles:
##                print title, '\n', links[0], '\n'
##                links.pop(0)
            for link in links:
                #print links
                if '.rdf' in link:
                    pass
                else:
                    #print link
                    print 'let\'s visit:', link
                    linkSource = opener.open(link).read()
                    #print linkSource
                    content = re.findall(r'<p>(.*?)</p>',linkSource)
                    for theContent in content:
                        print theContent

                    time.sleep(2)
                    

        except Exception, e:
            print str(e)

    except Exception, e:
        print str(e)


main()
