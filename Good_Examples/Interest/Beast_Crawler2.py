import urlparse
import urllib
from bs4 import BeautifulSoup
import csv
import requests
import re

x = 0

with open ("links.csv") as f:
        f_csv = csv.reader(f)

        for domains in f_csv:
                urls = domains
                urls_name = urls
                print type(urls)
                urls = "http://www." + str(domains[0])
                urls = urls.split()
                visited = [urls]
                urls_name = str(urls_name[0])
                urls_name = urls_name.replace("/", "")

                while len(urls) >0:
                        x = x+1
                        try:
                                htmltext = urllib.urlopen(urls[0]).read()
                        except:
                                print urls[0]

                        soup = BeautifulSoup(htmltext)

                        links = set()

                        '''
                        regex = '<title>(.+?)</title>'
                        pattern = re.compile(regex)
                        titles = re.findall(pattern,htmltext)
                        items = soup.findAll('a', href=True)                     
                        items2 = "STARTS HERE: " + '\n' + str(items)
                        saveFile = open ('crawl_findall.txt','a')
                        saveFile.write(str(urls)+ '\n')
                        saveFile.write(str(titles)+ '\n')
                        saveFile.write(str(items2) + '\n\n\n')
                        saveFile.close()                
                        print str(urls[0])
                        print str(titles)
                        print str(items2)
                        print '\n\n\n'
                        '''
                        with open(str(urls_name)+ str(x) + '.txt','a') as file:
                                for link in soup.findAll('a'):
                                    try:
                                        links.add(link['href'])
                                        print link.get_text()
                                        print link.get('href')
                                        print link.get('attr')
                                        print '\n'
                                        #file.write(link['href'] + "\n")
                                    except KeyError:
                                        pass
                                lis = str(list(links))
                                string = lis.split()
                                for i in string:
                                    print i
                                    print '\n'
                                    file.write(str(i) + "\n")
                        urls.pop(0)

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
