import requests
from bs4 import BeautifulSoup
# THIS IS THE WEB SCRAPPING
url = "https://fce.ufm.edu/carrera/cs/"
html_doc = requests.get(url)
# THIS CREATES THE SOUP OBJECT
soup = BeautifulSoup(html_doc.text,'html.parser')
print("3. computer science")

print("title is: ",soup.title.text)
a_tag = soup.find_all("a")
print ("number of a_tag is: ",len(a_tag))
div_tag = soup.find_all("div")
print ("number of a_tag is: ",len(div_tag))
cont = 0
for i in a_tag:
    cont = cont+1

print(cont)
