#http://searchcode.com/codesearch/view/43561492/
import urllib
import re
import os

def crawl(site, depth, linksfile):
  pattern = re.compile(r'href="(http://.*?)"')
  site_name = site
  site_name = str(site_name)
  site_name = site_name.replace("http://", "")
  site_name = linksfile
  f = open(linksfile + '.txt', 'a+')
  try: 
    if depth < MAX_DEPTH:
      print 'crawling [%s]...' % site, 
      print >> f, '[%s]' % site

      url = urllib.urlopen(site)
      content = url.read()
      hits = pattern.findall(content)
      for hit in hits:
        print >> f, hit
      print 'done.'
      print >> f, ''
      for hit in hits:
        crawl(hit, depth + 1, linksfile)
  except:
    pass
  f.close()

MAX_DEPTH=3
base = "https://query.nytimes.com/search/sitesearch/#/drone+strikes/"
#base = raw_input('Enter URL: ')


##
##if os.path.isfile(site_name):
##  os.remove(linksfile)
crawl(base, 1, linksfile)

