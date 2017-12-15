# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 01:51:47 2017

@author: Will Han
"""

import requests
from lxml import html
import collections
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import json
from textblob import TextBlob
import html2text
import pandas as pd



pg = []


for i in range(10):
    pg.append(i+1)

#LISTS
item_list = []
price_list = []
item_listraw = []
#seen= set()

for i in pg:
    print('https://www.walmart.com/search/?cat_id=0&page=' + str(i) + '&query=external+hard+drive#searchProductResult')
    
    url = requests.get('https://www.walmart.com/search/?cat_id=0&page=' + str(i) + '&query=external+hard+drive#searchProductResult')
    html_content = url.text
    soup = BeautifulSoup(html_content, 'lxml')
    item = soup.find_all(class_="product-title-link")
    price= soup.find_all(class_="price-main-block")
    
    
    for i in (item):
        item_listraw.append(i.get_text())
    for i in (price):
        price_list.append(i.get_text()) 
#    for i in (item):
#        if i not in seen:
#            item_list.append(i.get_text())
#            seen.add(i.get_text())

item_list = item_listraw[::2]

EHD_WM = pd.DataFrame({'Item': item_list,
                        'Price': price_list,})

#EHD_WM = pd.DataFrame({'Item': pd.Series(item_list).unique,
#                       'Price': pd.Series(price_list),})    
EHD_WM.to_csv('C:\DAPT\Text mining\Project\EHD_WM.csv')

