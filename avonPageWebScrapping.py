#class = flt_right desc_box transition_all_responsive
import re
import json

#urllib2
import requests as urllib2


#query the website and return the html to the variable 'page'
#page = urllib2.get(avon)
from bs4 import BeautifulSoup

#conexão com banco cosmetics
from dbConnection import *

#print(json.dumps(page.text, sort_keys=True, indent=4));

def printComposition(jsonText):
    copia = ''
    data = (page.text).split(',')
    for i in data:
        if '"Composição":[' in i:
            copia = i[15:-3]
    copia = copia.split('; ')
    for i in copia:
        print(i)
    print("--------------------")
'''
for i in range(20440,20450):
    actualPage = avon + str(i)
    
    printComposition(page.text)
'''




def populateDb():
    for productId in range(20000,30000):
        print(productId)
        #specify the base url : wich is avon store
        avon = "https://www.avonstore.com.br/api/catalog_system/pub/products/search/?fq=productId:"
        #transform into a requests page
        page = urllib2.get(avon + str(productId))
        pageText = page.text
        if(validatePageText(pageText)):
            #insertIntoDbCosmetics
            insertProduct(pageText,productId)

def validatePageText(pageText):
    if "[{" not in pageText:
        return False
    else:
        return True
    
    
def insertProduct(pageText,productId):
    #transform the page into text, and then into an array 
    data = (pageText).split(',')
    name = getNameAvon(data)
    brand = 'Avon'
    components = getComponentsAvon(data)
    categories = getCategories(pageText)
    img = getImg(data)
    link = getLink(data)
    cursor.execute('INSERT INTO products (product_id,name,brand,components,categories,img,link) VALUES (%s,%s,%s,%s,%s,%s,%s)',(str(productId),name,brand,components,categories,img,link))
    print("INSERT INTO succesful")
    connection.commit()
    
def getNameAvon(data):
    for i in data:
        if '"productName"' in i:
            name = i[15:-1]
            name = name.replace("\u2018","'").replace("\u2019","'").replace("\u2013","-")
            return name;
            
    return "no name"

def getComponentsAvon(data):
    for i in data:
        if '"Composição":[' in i:
            components = i[15:-3]
            if(len(components)>10):
                return components;
    return "no composition"

def getCategories(pageText):
    texto = pageText.split('categories')
    texto = texto[1].split(']')
    texto = texto[0]
    return texto

def getImg(data):
    for i in data:
        if '"imageUrl":"' in i:
            img = i[12:-1]
            return img;
    return "no image"

def getLink(data):
    for i in data:
        if '"link":"' in i:
            link = i[8:-1]
            link = link.replace("\u2018","'").replace("\u2019","'")
            return link;
    return "no link"


def printAll():
    cursor.execute('SELECT * FROM products')
    for l in cursor.fetchall():
        print(l)

populateDb()
connection.close()
    


