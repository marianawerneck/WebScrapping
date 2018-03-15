import requests
from bs4 import BeautifulSoup
deva = "http://devacurl.com.br/produtos/"
page = requests.get(deva)
soup = BeautifulSoup(page.text,'html.parser')

#pegar todos os link dos a's com a classe thumb
#print(soup.find_all("a",{"class":"thumb"}))

def createSoup(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def getName(soup):
    name = soup.find("h2").get_text()
    return name
    
def getComposition(soup):
    composition = soup.find(id="tab-test_tab").get_text()
    composition = composition[5:]
    return composition

def getImage(soup):
    a = soup.find("a",{"class":"woocommerce-main-image zoom"})
    img = a["href"]
    return img

def getCategory(soup):
    category = soup.find("span",{"class":"posted_in"}).contents[0].contents[0]
    return category

def getDescription(soup):
    description = soup.find("div",{"class":"product_description"}).contents[1]
    return description
                            
a_blocks = soup.find_all("a",{"class":"thumb"})
links = []
for a in a_blocks:
    if a.has_attr("href"):
        links.append(a["href"])

for link in links:
    soup = createSoup(link)
    print(getName(soup))
    print('-----------------------')
    print(getComposition(soup))
    print('-----------------------')
    print(getImage(soup))
    print('-----------------------')
    print(getCategory(soup))
    print('-----------------------')
    print(getDescription(soup))
    print('-----------------------')
    print('-----------------------')
    





