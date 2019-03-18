from urllib import urlopen
from HTMLParser import HTMLParser

class Scraper(HTMLParser):
    in_h3 = False
    in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag =='h3':
            self.in_h3 =True

        if tag == 'a' and 'href' in attrs:
            self.in_link = True
            self.chunk = []
            self.url = attrs['href']
            
    def handle_endtag(self, tag):
        if tag == 'h3':
            self.in_h3 = False

        if tag == 'a':
            if self.in_h3 and self.in_link:
                print '%s (%s)' %(''.json(self.chunks), self.url)
            self.in_link = False

text = urlopen('http://python.org/community/jobs').read()
parser = Scraper()
parser.feed(text)
parser.close()

