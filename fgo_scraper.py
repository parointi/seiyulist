"""Scrapes for roles from Fate/Grand Order"""

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

# create beautifulsoup object
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
url = "https://grandorder.wiki/Servants_by_Voice_Actors"
req = Request(url=url, headers=headers)
page = urlopen(req)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
