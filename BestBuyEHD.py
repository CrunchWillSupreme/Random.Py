# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 12:11:28 2017

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



pgBB = []


for i in range(10):
    pgBB.append(i+1)

#LISTS
item_listBB = []
price_listBB = []

for i in pgBB:
    print('https://www.bestbuy.com/site/searchpage.jsp?cp=' + str(i) + '&searchType=search&st=external%20hard%20drive&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All%20Categories&ks=960&keys=keys')
    
    urlBB = requests.get('https://www.bestbuy.com/site/searchpage.jsp?cp=' + str(i) + '&searchType=search&st=external%20hard%20drive&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All%20Categories&ks=960&keys=keys')
    html_contentBB = urlBB.text
    soupBB = BeautifulSoup(html_contentBB, 'lxml')
    itemBB = soupBB.find_all(class_="sku-title")
    priceBB= soupBB.find_all(class_="pb-hero-price pb-purchase-price")
    
    
    for i in (itemBB):
        item_listBB.append(i.get_text())
    for i in (priceBB):
        price_listBB.append(i.get_text()) 
        

EHD_BB = pd.DataFrame({'Item': item_listBB,
                        'Price': price_listBB,})

EHD_BB.to_csv('C:\DAPT\Text mining\Project\EHD_BB.csv')