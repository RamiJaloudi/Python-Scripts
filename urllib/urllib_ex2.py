import urllib

# This script runs on Python 2.7
# If using Python 3, please note that the urllib module has been split into parts and renamed as follows:
# urllib.request, urllib.parse, and urllib.error

url = "http://www.________.com" # Need to enter URL

request = urllib.urlopen(url)

response = request.read()

print response

