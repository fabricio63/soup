import requests
from bs4 import BeautifulSoup
url = "https://www.ufm.edu/Portal"
html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text,'html.parser')
a_tag = soup.find_all("a")
for i in a_tag :
    # print("---------------------------------------------------------------------------------------------------")
    print(i.text)
    
