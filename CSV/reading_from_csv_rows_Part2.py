
import re
import urlparse
import urllib
from bs4 import BeautifulSoup
import csv
import requests

with open ('data.csv') as f:

        f_csv = csv.reader(f)

        for headers in f_csv:
                urls = headers
                visited = [urls]


                while len(urls) >0:
                        try:
                                htmltext = urllib.urlopen(urls[0]).read()

                        except:
                                print urls[0]

                        soup = BeautifulSoup(htmltext)

                        #urls.pop(0)

                        items = soup.findAll('a', href=True)
                        
                        print headers

                        parsed = urlparse.urlparse(urls)
                        host = parsed.netloc.split('@')[-1].split(':')[0]
                        filepath = '%s%s' % (host, parsed.path)
                        if not os.path.splittext(parsed.path)[1]:
                                filepath = os.path.join(filepath, default)
                        linkdir = os.path.dirname(filepath)
                        if not os.path.isdir(linkdir):
                                if os.path.exists(linkdir):
                                        os.unlink(linkdir)
                                os.makedirs(linkdir)
                        #return url, filepath

                        items2 = "STARTS HERE:\n\n" + str(items)
                        saveFile = open (linkdir,'a')
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
