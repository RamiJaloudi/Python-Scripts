import requests

##res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res = requests.get('http://www.nytimes.com/pages/technology.txt')
print type(res)

# to see if the download succeeded
print res.status_code == requests.codes.ok

'''
# easier way to 
#res.raise_for_status()
    The raise_for_status() method is a good way to ensure that a program halts if a bad
    download occurs. This is a good thing: you want your program to stop as soon as some
    unexpected error happens. If a failed download isn’t a deal-breaker for your program, you can
    wrap the raise_for_status() line with try and except statements to handle this error case
    without crashing
'''
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

print len(res.text)

#print(res.text[:250])# Displays first 250 characters
print(res.text[:500])
