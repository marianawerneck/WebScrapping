#class = flt_right desc_box transition_all_responsive
import re
import json

#urllib2
import requests as urllib2
#specify the url
avon = "https://www.avonstore.com.br/renew-genics-creme-dia-fps-25-30g-avon-avn2000/p"
#query the website and return the html to the variable 'page'
page = urllib2.get(avon)
from bs4 import BeautifulSoup
#parse and store in bs4 format

patt = re.compile("var catalog\s+=\s+(\{.*?\});")



soup = BeautifulSoup(page.content, 'html.parser')
data2 = soup.find("script", text=re.compile("var catalog ="))
avon_js = json.loads(patt.search(data2).group(1))
print(avon_js)
print(soup.prettify())

