import nltk
import urllib
import readability
from bs4 import BeautifulSoup
#from readability.readability import Document
import mechanize

url = "http://www.nytimes.com/pages/national/index.html?action=click&pgtype=Homepage&region=TopBar&module=HPMiniNav&contentCollection=U.S.&WT.nav=page"

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]

html = br.open(url).read()

readable_article = Document(html).summary()
readable_title = Document(html).short_title()

soup = BeautifulSoup(readable_article)

final_article = soup.text

links = soup.findAll('img', src=True)

print final_article

#print readable_title
# print readable_article
