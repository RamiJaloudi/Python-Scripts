import nltk
import urllib
import readability
from bs4 import BeautifulSoup
from readability.readability import Document
import mechanize
import re, os


def crawl(site, depth, linksfile):
  pattern = re.compile(r'href="(http://.*?)"')
  f = open(linksfile, 'a+')
  try: 
    if depth < MAX_DEPTH:
      print 'crawling [%s]...' % site, 
      print >> f, '[%s]' % site

      br = mechanize.Browser()
      br.set_handle_robots(False)
      br.addheaders = [('User-agent', 'Firefox')]
      url = br.open(site)
      content = url.read()

      hits = pattern.findall(content)
      for hit in hits:
        print >> f, hit
        url2 = br.open(hit)
        content2 = url.read()
        readable_article = Document(content2).summary()
        readable_title = Document(content).short_title()
        soup = BeautifulSoup(readable_article)
        final_article = soup.text
        links = soup.findAll('img', src=True)
        print final_article
 
      print 'done.'
      print >> f, ''
      
      for hit in hits:

          crawl(hit, depth + 1, linksfile)
  except:
    pass
  f.close()

MAX_DEPTH=3
#base = raw_input('Enter URL: ')
base = r'http://www.nbcnews.com/storyline/new-york-prison-escape/second-n-y-prison-employee-arrested-following-jailbreak-convicted-killers-n381396'
linksfile = r'links.txt'

if os.path.isfile(linksfile):
  os.remove(linksfile)
crawl(base, 0, linksfile)
#print readable_title
# print readable_article
