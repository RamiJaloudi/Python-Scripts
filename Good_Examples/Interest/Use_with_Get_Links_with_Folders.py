# Python_Page_Spider_Web_Crawler_Tutorial
# from https://www.youtube.com/watch?v=SFas42HBtMg&list=PLa1r6wjZwq-Bc6FFb9roP7AZgzDzIeI8D&index=3
# Spider algorithm.
# You need to EXECUTE the file in Shell, e.g.  execfile("nytimes/scrape.py")
# First open cmd.  Then cd C:\Users\Joh\Documents\Python Scripts\Web Crawler Projects\nytimes.
# Then enter Python Scrape.py

import urlparse
import urllib
#import urllib.request for Python3?
from bs4 import BeautifulSoup
import csv
import requests
import re

with open ('links.csv') as f:
        f_csv = csv.reader(f)
        #headers = next(f_csv)

        for headers in f_csv:
                #print headers
                urls = headers
                urls_name = urls
                #print type(urls)
                urls = "http://www." + str(headers[0])
                urls = urls.split()
                urls_name = str(urls_name[0])
                urls_name = urls_name.replace("/", "")
                visited = [urls]
                #print urls
                #print type(urls)
                #print id(urls)
                #print '\n'
                
                while len(urls) >0:
                        try:
                                htmltext = urllib.urlopen(urls[0]).read()
                                #r = requests.get(urls[])
                                #urls.pop(0)
                        except:
                                print urls[0]

                        soup = BeautifulSoup(htmltext)

                        regex = '<title>(.+?)</title>'
                        pattern = re.compile(regex)
                        titles = re.findall(pattern,htmltext)

                        #urls.pop(0)

##                        print headers
##                        print "STARTS HERE:   \n"
##                        print "\n" + "\n"
##                        print soup.findAll('a', href=True)
##
##                        print "\n\n\n"

                        #items = soup.findAll('a', href=True)
                        textall = soup.get_text()

                        
                        print headers

                        def get_file(self, url, default='index.html'):
                                'Create usable local filename from URL'
                                parsed = urlparse.urlparse(headers)
                                host = parsed.netloc.split('@')[-1].split(':')[0]
                                filepath = '%s%s' % (host, parsed.path)
                                if not os.path.splitext(parsed.path)[1]:
                                        filepath = os.path.join(filepath, default)
                                linkdir = os.path.dirname(filepath)
                                if not os.path.isdir(linkdir):
                                        if os.path.exists(linkdir):
                                                os.unlink(linkdir)
                                        os.makedirs(linkdir)
                                return headers, filepath
                        
                        
                        #items2 = "STARTS HERE:\n\n" + str(items)
                        saveFile = open (str(urls_name)+'.txt','a')
                        saveFile.write(str(urls)+ '\n')
                        #saveFile.write(items2)
                        #saveFile.write(str(textall))
                        saveFile.write(str(titles)+ '\n')
                        saveFile.write(str(textall)+ '\n')
                        saveFile.close()
                        #print items
                        print textall

'''
        for tag in soup.findAll('a', href=True):
		# print tag
		# print tag['href'] # is you just want to print href
		tag['href'] = urlparse.urljoin(url,tag['href'])
		#print tag['href']
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href']) # historical record, whereas above line is temporary stack or queue.
		print visited	
'''
