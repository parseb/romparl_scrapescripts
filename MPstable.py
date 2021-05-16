#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:06:58 2020

@author: pb
"""

from bs4 import BeautifulSoup as soup
import urllib.request
from urllib.error import HTTPError
import re
import time

#"http://www.cdep.ro/pls/parlam/structura.mp?idm=253&cam=2&leg=2004"

tableurl='http://www.cdep.ro/pls/parlam/structura2015.ab?idl=1'
table_req = urllib.request.Request(url=tableurl, headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
table_handler = urllib.request.urlopen(table_req)
table_page_html= table_handler
page_soup= soup(table_page_html, "html.parser")

html_list=page_soup.find('.grup-parlamentar-list tbody')

mp_table=page_soup.find_all('tr')
hrefs=[i.a['href'] for i in mp_table[2:]]


#mp_table22=[i.a['href'] for i in mp_table]
mp_table2= [i.text.split('\n') for i in mp_table[2:]]

c=0
for i in mp_table2:
    mp_table2[c].append(hrefs[c])
    c=c+1
    
mp_table3= [i for i in mp_table2 if len(i)>5]


import pandas as pd

#name link dpt/sen  drop: period
df= pd.DataFrame.from_records(mp_table3, columns=['0','num','name','period','',5,6])
df.to_csv('ALL_MP.csv')



