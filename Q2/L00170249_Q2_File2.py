"""
#
# File       : Q2_L00170249_heading.py
# Created    : 14/11/2021 20:53
# Author     : S.Dunne
#
# Description: Scrape Apache 2 website and pull the Website title
#
"""
import requests
from bs4 import BeautifulSoup

...
url = "http://172.16.253.135"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print("Title of the website is : ")
for heading in soup.find_all('title'):
    print(heading.get_text())
