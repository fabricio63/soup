import requests
from bs4 import BeautifulSoup
url = "https://www.ufm.edu/Portal"
html_doc = requests.get(url)
# THIS CREATES THE SOUP OBJECT
soup = BeautifulSoup(html_doc.text,'html.parser')
res = []
for i in soup.find_all("div"):
    n = i.get('class')
    if type(n) == list:
        if n[0] == 'menu-key':
            r = i.get('data-menu')
            if r != None :
                print(r)




