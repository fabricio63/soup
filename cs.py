import requests
import shutil
from time import sleep
from bs4 import BeautifulSoup
# THIS IS THE WEB SCRAPPING
url = "https://fce.ufm.edu/carrera/cs/"
html_doc = requests.get(url)
# THIS CREATES THE SOUP OBJECT
soup = BeautifulSoup(html_doc.text,'html.parser')

# This is the image url.
image_url = "https://fce.ufm.edu/carrera/wp-content/uploads/2017/10/MapaLogotipos-CIENCIAS-ECONOMICAS_1H-1Col-Inv.png"
# Open the url image, set stream to True, this will return the stream content.
resp = requests.get(image_url, stream=True)
# Open a local file with wb ( write binary ) permission.
local_file = open('logo.jpg', 'wb')
# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
resp.raw.decode_content = True
# Copy the response stream raw data to local image file.
shutil.copyfileobj(resp.raw, local_file)
print("==============================")
print("3. computer science")

print("title is: ",soup.title.text)
a_tag = soup.find_all("a")
print("")
print ("number of a_tag is: ",len(a_tag))
print("")
div_tag = soup.find_all("div")
print ("number of a_tag is: ",len(div_tag))
print("")
print("downloading image (name will be logo.png)")
sleep(1.5)


