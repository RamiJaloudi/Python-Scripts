
'''
import urllib.request
req = urllib.request.Request('http://www.voidspace.org.uk')
response = urllib.request.urlopen(req)
the_page = response.read()
'''

import urllib.request
req = urllib.request.Request('http://www.cnn.com')
response = urllib.request.urlopen(req)
the_page = response.read()
