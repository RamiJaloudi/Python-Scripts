# from xml.dom.minidom import parse, parseString
# import urllib
# note - i convert it back into xml to pretty print it
# print parse(urllib.urlopen("http://search.twitter.com/search.atom?&q=python")).toprettyxml(encoding="utf-8")


import urllib.request
response = urllib.request.urlopen('http://www.craigslist.com/')
html = response.read()


'''
import urllib.request
local_filename, headers = urllib.request.urlretrieve('http://www.craigslist.com')
html = open(local_filename)
'''
