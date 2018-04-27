#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup

def googlenews():
        url = 'https://news.google.com/news/'
        r = requests.get(url)
        content = r.text
        soup = BeautifulSoup(content,"html.parser")
        f = open('test.txt', 'w')
        f.write(soup.prettify())
        f.close()
        headlines = soup.find_all('a',{'class':'nuEeue hzdq5d ME7ew'})
        f = open('news.txt','w')
        for headline in headlines:
            f.write(headline.string + '\n')
            f.write(headline.get('href') + '\n')
        f.close()
        pubs = soup.find_all('span',{'class':'IH8C7b Pc0Wt'})
        f = open('pubs.txt','w')
        for pub in pubs:
            f.write(pub.string + '\n')
        f.close()

def main():
    try:
        googlenews()
    except:
        print("Failed.")

if __name__ == '__main__':
    main()
