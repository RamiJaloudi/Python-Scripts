# This script used the regex and urllib modules to crawl a list of sites.
# It simply provides the title tags, i.e., titles you would see on web browser tabs.

import re, urllib
try:
    import urllib.request
except:
    pass

sites = 'cnn nytimes bloomberg'.split()

pat = re.compile(r'<title>.+?</title>+', re.I|re.M)

for s in sites:
    print('Searching:' + s)
    try:
        u = urllib.urlopen('http://' + s + '.com')
    except:
        u = urllib.request.urlopen('http://' + s + '.com')
    text = u.read()
    title = re.findall(pat, str(text))
    print title
    print '\n'
