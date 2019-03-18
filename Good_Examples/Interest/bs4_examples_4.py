from bs4 import BeautifulSoup
import sys
import os
import requests
from ast import literal_eval

def get_links(url):

    r = requests.get(url)
    contents = r.content

    soup = BeautifulSoup(contents)
    links =  set()
    with open("links_methods.txt", "a") as file:
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

def restart_program():
     """Restarts the current program.
     Note: this function does not return. Any cleanup action (like
     saving data) must be done before calling this function."""
##     python = sys.executable
##     os.execl(python, python, * sys.argv)
     url = raw_input('Enter url starting without http:// - ')
     url = "http://" + url
     print get_links(url)

	 
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



