#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:21:08 2020

@author: pb
"""

import pandas as pd
from bs4 import BeautifulSoup as soup
import urllib.request
from urllib.error import HTTPError
import re
import time

df1= pd.read_csv('ALL_MP.csv')

urls= df1['6'][2020:] #dropped at 2019
party=[]
yr_born=[]
progress=0
def getparty(urll):
        #party
        
        table_req = urllib.request.Request(url=urll, headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
        table_handler = urllib.request.urlopen(table_req)
        table_page_html= table_handler
        page_soup= soup(table_page_html, "html.parser")
        party.append(page_soup.find_all('div', {'class':'boxDep'})[1].text.split('\n')[1])
        #yr_b
        urll=i.replace('structura2015','structura')
        table_req = urllib.request.Request(url=urll, headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
        table_handler = urllib.request.urlopen(table_req)
        table_page_html= table_handler
        page_soup= soup(table_page_html, "html.parser")
        yr_born.append(page_soup.find_all('td',{'class':'menuoff'})[0].text.split(' ')[-1])
        
        
for i in urls:
    i= 'http://www.cdep.ro'+i
    getparty(i)
    time.sleep(2)
    print(progress)
    progress=progress+1
    
df1['party']= party[0:-1] #[0:-1]    
df1['yearb']= yr_born

df1.to_csv('MPsWparty_yeartest.csv')



########### 
urll='http://cdep.ro/pls/parlam/structura.mp?idm=348&cam=2&leg=2016'
#urll='http://cdep.ro/pls/parlam/structura2015.mp?idm=5&leg=2012&cam=2'    
table_req = urllib.request.Request(url=urll, headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
table_handler = urllib.request.urlopen(table_req)
table_page_html= table_handler
page_soup= soup(table_page_html, "html.parser")

#yr dob
page_soup.find_all('td',{'class':'menuoff'})[0].text.split(' ')[-1]




