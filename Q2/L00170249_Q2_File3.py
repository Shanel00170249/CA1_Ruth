"""
#
# File       : Q2_L00170249_scrape.py
# Created    : 04/11/2021 20:09
# Author     : S.Dunne
#
# Description: Scrape Apache 2 web page and parse the output
#
"""
import urllib.request
from bs4 import BeautifulSoup

url = "http://172.16.253.135/"  # vm ip address

html = urllib.request.urlopen(url)
htmlParse = BeautifulSoup(html, 'html.parser')

for para in htmlParse.find_all("p"):
    print(para.get_text())
