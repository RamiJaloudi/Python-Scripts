import nltk
import urllib
import readability
from bs4 import BeautifulSoup
from readability.readability import Document

url = 'https://news.google.com/nwshp?hl=en&tab=wn&ei=VWFsVdiLMMiXyATEyIPIBQ&ved=0CAUQqS4oBQ'

html = urllib.urlopen(url).read()


readable_article = Document(html).summary()
readable_title = Document(html).short_title()

soup = BeautifulSoup(readable_article)

final_article = soup.text

##links = soup.findAll('img', src=True)

print final_article
##print links
##
##print readable_title
#print readable_article
