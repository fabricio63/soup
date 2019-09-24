import requests
import shutil
from time import sleep
from bs4 import BeautifulSoup
# THIS IS THE WEB SCRAPPING
url = "https://ufm.edu/Estudios"
html_doc = requests.get(url)
# THIS CREATES THE SOUP OBJECT
soup = BeautifulSoup(html_doc.text,'html.parser')
div_social = soup.find("div", class_ = "social pull-right")
div_text = div_social.find_all("a")
lista_links = []
for i in div_text:
    lista_links.append(i['href'])

print("linkedin links to: ", lista_links[0])
print("facebook links to: ", lista_links[1])
print("twitter links to: ", lista_links[2])
print("google links to: ", lista_links[3])
print("youtube links to: ", lista_links[4])
print("pinterest links to: ", lista_links[5])
    
    

