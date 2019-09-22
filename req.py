import requests
from bs4 import BeautifulSoup
# THIS IS THE WEB SCRAPPING
url = "https://ufm.edu/Estudios"
html_doc = requests.get(url)
# THIS CREATES THE SOUP OBJECT
soup = BeautifulSoup(html_doc.text,'html.parser')
a_tag = soup.find_all("a",)


for i in a_tag :
    
    print(i.text)
