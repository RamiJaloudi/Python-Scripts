# Version 3.4
import re
import os, sys, glob
from os import system
from urllib.request import urlopen



page = urlopen("http://love-python.blogspot.com/2008/07/strip-html-tags-using-python.html").read()
myfile = open('testfile.txt', 'w')
fileencoding = "iso-8859-1"
txt = page.decode(fileencoding)

def remove_html_tags(txt):
    p = re.compile(r'<[^<]*?/?>')
    return p.sub('', txt)
myfile.write(txt)
