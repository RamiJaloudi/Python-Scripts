import urllib # this is a GET
x = urllib.urlopen('https://www.google.com/#q=nj+laws')
print(x.read())
# urlparse Module - urlparse(urlstr, defProtSCh=None, allowFrag=None)
# urlparse() breaks a URL into a 6-tuple (prot_sch, net_loc, path params, query, frag)
# defProtSh indidcates a default network protocol or download scheme in case one is not provided in urlstr.
# allFrag is a flag that signals whether or not a fragment part of a URL is allowed.

'''
import urllib.request
response = urllib.urlopen('http://python.org/')
html = response.read()
'''

'''
import urllib.request
local_filename, headers = urllib.request.urlretrieve('http://python.org/'
html = open(local_filename)
'''
