"""
#
# File       : Q2_L00170249_wordcount.py
# Created    : 15/11/2021 17:41
# Author     : S.Dunne
#
# Description: Count the number of times Apache2 appears on the website
#
"""

import requests
from bs4 import BeautifulSoup

url = "http://172.16.253.135"  # ip of vm
the_word = 'Apache2'  # the word to search for
r = requests.get(url, allow_redirects=False)
soup = BeautifulSoup(r.content, "html.parser")
words = soup.find(text=lambda text: text and the_word in text)
print(words)
count = len(words)
print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, the_word))
