import requests
from bs4 import BeautifulSoup
deva = "http://devacurl.com.br/produtos/"
page = requests.get(deva)
soup = BeautifulSoup(page.text,'html.parser')

#pegar todos os link dos a's com a classe thumb
#print(soup.find_all("a",{"class":"thumb"}))

links = soup.find_all("a",{"class":"thumb"})
for i in links:
    if i.has_attr("href"):
        print(i["href"])
