## import ssl
## Not working if you see the following error:
## ImportError: No module named _ssl

import urllib3
import certifi

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED', # Force certificate check.
    ca_certs=certifi.where(),  # Path to the Certifi bundle.
)

# You're ready to make verified HTTPS requests.

try:
    r = http.request('GET', 'https://example.com/')
except urllib3.exceptions.SSLError as e:
    print e
    # Handle incorrect certificate error

