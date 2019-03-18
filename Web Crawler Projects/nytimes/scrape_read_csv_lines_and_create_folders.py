# Version 2.7
# Web Scraper
# Need csv containing links; csv file saved as "data.csv"

import urlparse
import urllib
#import urllib.request for Python3?
from bs4 import BeautifulSoup
import csv
import requests

with open ('data.csv') as f:
        f_csv = csv.reader(f)
        #headers = next(f_csv)

        for headers in f_csv:
                #print headers
                urls = headers
                visited = [urls]

                while len(urls) >0:
                        try:
                                htmltext = urllib.urlopen(urls[0]).read()
                                #r = requests.get(urls[])
                                #urls.pop(0)
                                htmlDoc = "STARTS HERE:\n\n" + str(items)
                                saveFile = open ('htmlDoc.txt','w')
                                saveFile.write(htmlDoc)
                                saveFile.close()
                                print htmlDoc
                        except:
                                print urls[0]

                        soup = BeautifulSoup(htmltext)

                        urls.pop(0)

                        print headers
                        print "STARTS HERE:   \n"
                        print "\n" + "\n"
                        print soup.findAll('a', href=True)

                        print "\n\n\n"

                        items = soup.findAll('a', href=True)
                        
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
                        
                        
                        items2 = "STARTS HERE:\n\n" + str(items)
                        saveFile = open ('crawl_findall.txt','w')
                        saveFile.write(items2)
                        saveFile.close()
                        print items2

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
