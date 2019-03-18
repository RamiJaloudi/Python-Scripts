import urllib
import re

urls = ["https://www.google.com/#q=nj+laws"]
i=0
regex = '<title>(.+?)</title>'
regex2 = '<p>(.+?)</p>'
regex3 = '<script>(.+?)</script>'
pattern = re.compile(regex)
pattern2 = re.compile(regex2)
pattern3 = re.compile(regex3)

while i< len(urls):
    htmlfile = urllib.urlopen(urls[i])
    htmltext = htmlfile.read()
    titles = re.findall(pattern, htmltext)
    paragraphs = re.findall(pattern2, htmltext)
    scripts = re.findall(pattern3, htmltext)

    print titles
    #print htmltext
    print paragraphs
    print scripts
    i+=1
