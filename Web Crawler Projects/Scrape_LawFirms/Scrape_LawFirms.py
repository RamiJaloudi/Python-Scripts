import urllib
from bs4 import BeautifulSoup

url = "https://query.nytimes.com/search/sitesearch/?action=click&contentCollection&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=Homepage#/drone strikes"

htmltext=urllib.urlopen(url)
#htmltext = requests.get(urls)
soup = BeautifulSoup(htmltext)
saveFile = open('soup.txt','a')
saveFile.write(str(soup)+ '\n')
saveFile.close()
