#!/usr/bin/python

import urllib  # could import it with alias
import sys

from bs4 import BeautifulSoup # This is a third party library
from Problem import Problem

def debug(msg):
    # print msg
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()

def problems_list(URL):
    '''
    This functions takes a spoj problems page url, and returns a list of Problem instances.
    '''
    debug("Fetching html....")
    html_data = urllib.urlopen(URL).read()
    debug("Html fetched, prettifying results....")
    soup = BeautifulSoup(html_data, 'html.parser')
    table = soup.find('table', attrs={'class': 'problems'})
    problems_list = table.find('tbody').findAll('tr')
    debug("In the middle of parsing....")
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
        instance = Problem(pid, pname, plink, quality, users, accuracy)
        problems.append(instance)
    debug("Done!")
    return problems
