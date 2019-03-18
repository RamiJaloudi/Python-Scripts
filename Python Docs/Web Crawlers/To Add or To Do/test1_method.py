from bs4 import BeautifulSoup
import urllib

def response(url):
        webpage = urllib.urlopen(url)
        response = webpage.read()
        soup = BeautifulSoup(response.text)
        
        return soup

if __name__=='__main__':
    print response('http://nytimes.com')
