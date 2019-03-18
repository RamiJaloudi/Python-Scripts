import urllib
from html2text import html2text


for line in html2text(urllib.urlopen("http://moviebodycounts.com/Blood_Diamond.htm").read()).split("\n"):
    if "IMDb" in line:
        print line.split("[IMDb]")[1].strip("(").strip(",").strip(")")
    if "Film:" in line:
        print line.split("Film:")[-1].strip()
