import requests
from bs4 import BeautifulSoup
# THIS IS THE WEB SCRAPPING
url = "https://www.ufm.edu/Portal"
html_doc = requests.get(url)
# THIS CREATES THE SOUP OBJECT
soup = BeautifulSoup(html_doc.text,'html.parser')
# THIS GETS TITLE
title = soup.title.string
# THIS GETS ADDRESS
meta = soup.find_all("meta",limit = 8)
for i in meta:
    si = str(i)
    if si == '<meta content="https://www.ufm.edu" property="og:url"/>':
        link_line = BeautifulSoup(si,'html.parser')
link_attrs = link_line.meta
link_name = link_attrs['content']

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////

link_tag = soup.find_all("link")
a_tag = soup.find_all("a")
img_tag = soup.find_all("img")
def print_refs(tags):
    for i in tags :
        print("---------------------------------------------------------------------------------------------------")
        print("   - ",i['href'])
  

for i in a_tag :
    if i['href'] =="tel:+50223387700":
        number_name = i['href']
    no = str(i)
    if no == '<a href="mailto:inf@ufm.edu" style="color:#333;">inf@ufm.edu</a>':
        mail_line = BeautifulSoup(no,'html.parser')
    if i.text == "UFMail":
        button_name = i['href']
    if i.text == "MiU":
        button_MIU = i['href']
mail_attrs = mail_line.a
mail_name = mail_attrs['href']


print("")
print("< Fabricio Juarez >")
print("=====================")
print("1.portal")
print ("        title is: ",title)   
print("")
print ("        mail is: ",mail_name)
print("")
print ("        adress is: ",link_name)   
print("")
print ("       ",number_name)   
print("")
print ("        email button is : ",button_name)  
print("")
print ("        MIU button is : ",button_MIU)  
print("")
print ("        a_tag length is: ",len(a_tag)) 
print("")


if (len(link_tag)+len(a_tag)) < 30:
    print("hrefs are:")
    print_refs(link_tag)
    print_refs(a_tag)
else:
    print("creating txt file for href and img sources (file name is href.txt)")
    f = open("href.txt","w+")
    f.write("hrefs are: ")
    f.write('\n')
    for i in link_tag:
        writing =i['href']
        f.write(writing)
        f.write('\n')
        
    for i in a_tag:
        writing = i['href']
        f.write(writing)
        f.write('\n')
    f.write('\n')
    f.write("img sources are:")
    f.write('\n')
    for i in img_tag:
        writing = i['src']
        f.write(writing)
        f.write('\n')    
        


        
