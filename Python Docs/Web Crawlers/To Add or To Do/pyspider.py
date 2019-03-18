

##usage is pyspider.py site link
##     improved version based on http://www-128.ibm.com/developerworks/linux/library/l-spider/
##     I found this link and shined it up a bit.
##     added:
##      ignores list. Just put your own prefs in.
##      ignoring links with # sign
##      only read html pages based on httpconn.response insted off suffix .htm


import httplib
import sys
import re
from HTMLParser import HTMLParser

class miniHTMLParser( HTMLParser ):

    ignores =  [ "mailto:", "login_form", "sendto", "orig_query", "ploneglossary", "search", "search", "language" , "Language" ]
    viewedQueue = {} # Dict to secure uniqness and a bid faster.
    instQueue = []

    def __init__( self, site="" ):
      HTMLParser.__init__(self)
      self.site = site

    def get_next_link( self ):
      if self.instQueue == []:
        return ''
      else:
        return self.instQueue.pop(0)


    def gethtmlfile( self, site="", page="" ):
        httpconn = httplib.HTTPConnection(site)
        try:
          httpconn.request("GET", page)
        except:
          print """Trouble with: httpconn.request("GET", page)""", page
          return ""
        resp = httpconn.getresponse()
        if resp.msg.type.rfind("text/html") > -1:
          # Only care about html files
          return resp.read()
        return ""

    def handle_starttag( self, tag, attrs ):
      if tag == 'a':
        for at in attrs:
          if at[0] == "href":
              newstr = at[1]
              if self.viewedQueue.has_key(newstr ):
                  return
              else:
                  self.viewedQueue[newstr] = 1
                  for ignore in self.ignores:
                      if newstr.rfind(ignore) > -1:
                          return
              break
        else:
          return

        if (  newstr.rfind( self.site ) > -1 \
           or newstr.rfind( "http:" ) < 0 ) \
         and newstr.rfind( '#' )  < 0  : # ignore internal page refs
            self.instQueue.append( newstr )

def main():

    if len(sys.argv) < 2 :
      print __doc__
      sys.exit(2)

    site = sys.argv[ 1 ]
    link = sys.argv[ 2 ]

    mySpider = miniHTMLParser(site)
    while link != '':

      print "\nChecking link ", link

      # Get the file from the site and link
      retfile = mySpider.gethtmlfile( site=site, page=link )

      # print retfile # XXX
      # Feed the file into the HTML parser
      mySpider.feed(retfile)

      # Search the retfile here

      # for ix in mini.HTMLParser.
      # Get the next link in level traversal order
      link = mySpider.get_next_link()

    mySpider.close()

    print "\ndone\n"

if __name__ == "__main__":
    main()
