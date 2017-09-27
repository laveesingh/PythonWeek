#!/usr/bin/python
'''
Author: Lavee Singh
Description: This script has fixed url and scrapes probelm list from that url and prints all those problems.
'''

import urllib  # could import it with alias
import sys

from bs4 import BeautifulSoup # This is a third party library

def debug(msg):
    # print msg
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()

URL = "http://www.spoj.com/problems/classical/"

debug("Fetching html...")
html_data = urllib.urlopen(URL).read()
debug("Html fetched...")

soup = BeautifulSoup(html_data, 'html.parser')
table = soup.find('table', attrs={'class': 'problems'})
problems_list = table.find('tbody').findAll('tr')

problems = []
for problem in problems_list:
    col_list = problem.findAll('td')
    pid = col_list[0].string.strip()
    plink = 'http://www.spoj.com' + col_list[1].find('a').get('href')
    pname = col_list[1].find('a').string.strip()
    try:
        quality = col_list[2].find('span').find('strong').string.strip()
    except AttributeError:
        quality = 'undefined'
    users = col_list[3].find('a').string.strip()
    accuracy = col_list[4].find('a').string.strip()
    print pid, pname, quality, users, accuracy, plink

debug("Done!")
