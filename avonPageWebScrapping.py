#class = flt_right desc_box transition_all_responsive
import re
import json

#urllib2
import requests as urllib2
#specify the url
avon = "https://www.avonstore.com.br/api/catalog_system/pub/products/search/?fq=productId:20441"
#query the website and return the html to the variable 'page'
page = urllib2.get(avon)
from bs4 import BeautifulSoup

#print(json.dumps(page.text, sort_keys=True, indent=4));

data = (page.text).split(',')
for i in data:
    if '"Composição":[' in i:
        copia = i[15:-3]
copia = copia.split('; ')
for i in copia:
    print(i)
