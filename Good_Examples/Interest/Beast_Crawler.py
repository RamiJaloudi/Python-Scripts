from bs4 import BeautifulSoup
import csv, os, requests, sys
from ast import literal_eval

def get_links(url):

        r = csv.reader(open("links.csv"))

        url_queue

        for row in r:
                url_queue.append(row[2])
                urls_name = urls
                #print type(urls)
                urls = "http://www." + str(headers[0])
                urls = urls.split()
                urls_name = str(urls_name[0])
                urls_name = urls_name.replace("/", "")
            
        url = url_queue

        urls = [url] #stack of urls to scrape

        visited = [url] #historical record of urls

        while len(urls) >0:
                try:
                #htmltext=urllib.request.urlopen(url[0])
                #htmltext = requests.get(urls)
                        req = requests.get(url[0])
                        contents = r.content
                except:
                        print (urls[0])

                soup = BeautifulSoup(htmltext)
                        
                links =  set()
                
                with open(str(urls_name)+'.txt','a') as file:
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
                            #file.write(link['href'] + "\n")
                            #file.write(str(links) + "\n")
                        #return links
                        
                        lis = str(list(links))
                        string = lis.split()
                        for i in string:
                            print i
                            print '\n'
                            file.write(str(i) + "\n")


if __name__ == "__main__":
        get_links(url)
        
'''
def restart_program():
     """Restarts the current program.
     Note: this function does not return. Any cleanup action (like
     saving data) must be done before calling this function."""
##     python = sys.executable
##     os.execl(python, python, * sys.argv)
     url = raw_input('Enter url starting without http:// - ')
     url = "http://" + url
     print get_links(url)
'''


''' 
if __name__ == "__main__":
    while 1==1:
        url = raw_input('Enter url starting without http:// - ')
        url = "http://" + url
        print get_links(url)
        answer = raw_input("Do you want to restart this program ? ")
        if answer.lower().strip() in "y yes".split():
            restart_program()
        if answer.lower().strip() in "n no".split():
            sys.exit()
##        url = raw_input('Enter url: ')
##        print get_links(url)
'''


