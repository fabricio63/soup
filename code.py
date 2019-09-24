import requests
from bs4 import BeautifulSoup
from time import sleep
import shutil
# THIS IS THE WEB SCRAPPING
def print_refs(tags):
        for i in tags :
            print("---------------------------------------------------------------------------------------------------")
            print("   - ",i['href'])
def portal():
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
    print("====================================================================================================================")
    print("1.portal")
    print("        title is: ",title)   
    print("--------------------------------------------------------------------------------------------------------")
    
    print ("        mail is: ",mail_name)
    print("--------------------------------------------------------------------------------------------------------")

    print ("        adress is: ",link_name)   
    print("--------------------------------------------------------------------------------------------------------")
    print ("       ",number_name)   
    print("--------------------------------------------------------------------------------------------------------")
    print ("        email button is : ",button_name)  
    print("--------------------------------------------------------------------------------------------------------")
    print ("        MIU button is : ",button_MIU)  
    print("")
    print ("        a_tag length is: ",len(a_tag)) 
    print("--------------------------------------------------------------------------------------------------------")
    print("        nav bar buttons are: ")
    for i in soup.find_all("div"):
        n = i.get('class')
        if type(n) == list:
            if n[0] == 'menu-key':
                r = i.get('data-menu')
                if r != None :
                    print("                                - ",r)

    if (len(link_tag)+len(a_tag)) < 30:
        print("hrefs are:")
        print_refs(link_tag)
        print_refs(a_tag)
    else:
        print("")
        print("creating txt file for href and img sources (file name is href.txt)")
        f = open("C:\logs\href.txt","w+")
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

def finder(tag,keye):
        for i in tag :
            if i.text == keye:
                print("--------------------------------------------------------------------------------------------------------")
                print(keye," links to ",i['href'])

def estudio():
    # THIS IS THE WEB SCRAPPING
    url = "https://ufm.edu/Estudios"
    html_doc = requests.get(url)
    # THIS CREATES THE SOUP OBJECT
    soup = BeautifulSoup(html_doc.text,'html.parser')
    a_tag = soup.find_all("a",limit = 8)
    a_tag28 = soup.find_all("a")
    a_tag100 = soup.find_all("a",limit = 100)
    a_tag150 = soup.find_all("a",limit = 300)
    print("====================================================================================================================")
    print ("2.estudios")
    #fdsffsfsfs
    f = open("estudios.txt","w+")
    def finder_txt(tag,keye):
        for i in tag :
            if i.text == keye:
                f.write("--------------------------------------------------------------------------------------------------------")
                f.write('\n')
                f.write(i['href'])
                f.write('\n')
                
            
    print("")
    print("top bar icons are: ")
    finder(a_tag,"UFM Key Projects")
    finder(a_tag,"Friends of UFM")
    finder(a_tag,"Donaciones")
    finder(a_tag,"Contáctenos")
    finder(a_tag,"Admisiones")
    finder(a_tag,"Alumni")
    finder(a_tag,"Campus Madrid")
    finder(a_tag,"Redes Sociales")
    print("--------------------------------------------------------------------------------------------------------")
    print("IMPRIMIENDO ESTUDIOS A ESTUDIOS.TXT")
    f.write("Doctorados son:")
    f.write('\n')
    finder_txt(a_tag28,"Programa de Doctorado")
    f.write("")
    f.write("Maestrias son:")
    f.write('\n')
    finder_txt(a_tag28,"MBA in Entrepreneurship")
    finder_txt(a_tag28,"Arbitraje Internacional")
    finder_txt(a_tag28,"Ciencias Sociales")
    finder_txt(a_tag28,"Génetica Molecular Humana")
    finder_txt(a_tag28,"Psicología Médica Integral")
    finder_txt(a_tag28,"MBA")
    finder_txt(a_tag28,"MBA Virtual")
    finder_txt(a_tag28,"MFIN")
    finder_txt(a_tag28,"MAPI")
    finder_txt(a_tag28,"LLM")
    finder_txt(a_tag28,"MEE")
    finder_txt(a_tag28,"ME")
    finder_txt(a_tag28,"Diabetes y Síndrome Metabólico")
    finder_txt(a_tag28,"Enfermedad Renal Crónica y Síndrome")
    finder_txt(a_tag28,"Metabólico")
    finder_txt(a_tag28,"Filosofía")
    finder_txt(a_tag28,"Historia")
    finder_txt(a_tag28,"Lingüistica")
    finder_txt(a_tag28,"Objetivismo")
    finder_txt(a_tag28,"Política Económica Internacional")
    finder_txt(a_tag28,"Política y Derecho Internacional")       
    finder_txt(a_tag28,"Relaciones internacionales")
    finder_txt(a_tag28,"Endodoncia")
    finder_txt(a_tag28,"Ortodoncia")
    finder_txt(a_tag28,"Rehabilitación Oral y Odontología Cosmética")
    finder_txt(a_tag28,"Periodoncia e Implantes Dentales")
    f.write("\n")
    f.write("posgrados son: ")
    f.write('\n')
    finder_txt(a_tag28,"Dermatología")
    finder_txt(a_tag28,"Hemato-Oncología Pediátrica")
    finder_txt(a_tag28,"Medicina Interna")
    finder_txt(a_tag28,"Oftalmología")
    finder_txt(a_tag28,"Historia")
    finder_txt(a_tag28,"Lingüística")
    f.write("\n")
    f.write("licenciaturas son: ")
    f.write('\n')
    finder_txt(a_tag28,"Administración de Empresas")
    finder_txt(a_tag28,"Finanzas")
    finder_txt(a_tag28,"Mercadeo")
    finder_txt(a_tag28,"Arquitectura")
    finder_txt(a_tag28,"Ciencia Política")
    finder_txt(a_tag28,"Comercio Exterior")
    finder_txt(a_tag28,"Comunicación y Periodismo")
    finder_txt(a_tag28,"Políticas Públicas")
    finder_txt(a_tag28,"Gestión de Proyectos")
    finder_txt(a_tag28,"Contaduría Pública y Auditoría (CPA)")
    finder_txt(a_tag28,"Derecho")
    finder_txt(a_tag28,"Diseño de Producto")
    finder_txt(a_tag28,"Diseño Digital Interactivo")
    finder_txt(a_tag28,"Economía")
    finder_txt(a_tag28,"Data Science")
    finder_txt(a_tag28,"Politics and Philosophy")
    finder_txt(a_tag28,"Educación y Emprendimiento")
    finder_txt(a_tag28,"Enseñanza de la Historia")
    finder_txt(a_tag28,"Entrepreneurship and Business")
    finder_txt(a_tag28,"Escuela de Cine y Artes Visuales")
    finder_txt(a_tag28,"BA en Cine, Artes Visuales y Emprendimiento")       
    finder_txt(a_tag28,"Ingeniería Empresarial")
    finder_txt(a_tag28,"Ingeniería en Computer Science")
    finder_txt(a_tag28,"Lengua y Literatura")
    finder_txt(a_tag28,"Medicina")
    finder_txt(a_tag28,"Nutrición Clínica")
    print(("--------------------------------------------------------------------------------------------------------"))
    print("left bar icons are:")
    finder(a_tag100,"Biblioteca")
    finder(a_tag100,"New Media")
    finder(a_tag100,"Calendario")
    finder(a_tag100,"Directorio")
    print("--------------------------------------------------------------------------------------------------------")
    print("a_tag length is:",len(a_tag28))
    ("--------------------------------------------------------------------------------------------------------")
    print("links to social media are: ")
    div_social = soup.find("div", class_ = "social pull-right")
    div_text = div_social.find_all("a")
    lista_links = []
    for i in div_text:
        lista_links.append(i['href'])
   
    print("- linkedin links to: ", lista_links[0])
   
    print("- facebook links to: ", lista_links[1])
   
    print("- twitter links to: ", lista_links[2])
   
    print("- google links to: ", lista_links[3])
   
    print("- youtube links to: ", lista_links[4])
   
    print("- pinterest links to: ", lista_links[5])
        

def css():
    # THIS IS THE WEB SCRAPPING
    url = "https://fce.ufm.edu/carrera/cs/"
    html_doc = requests.get(url)
    # THIS CREATES THE SOUP OBJECT
    soup = BeautifulSoup(html_doc.text,'html.parser')
    img_tag = soup.find_all('img')
    for i in img_tag:
        result = i['src'].endswith("MapaLogotipos-CIENCIAS-ECONOMICAS_1H-1Col-Inv.png")
        if result == True:
            image_url = i['src']
    resp = requests.get(image_url, stream=True)
    local_file = open('logo.jpg', 'wb')
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    print("====================================================================================================================")
    print("3. computer science")

    print("title is: ",soup.title.text)
    a_tag = soup.find_all("a")
    print("--------------------------------------------------------------------------------------------------------")
    print ("number of a_tag is: ",len(a_tag))
    print("--------------------------------------------------------------------------------------------------------")
    title = soup.find("meta", property = "og:title")
    print ("og:title is ",title['content'])
    print("--------------------------------------------------------------------------------------------------------")
    description = soup.find("meta", property = "og:description")
    print ("og:description is ",description['content'])
    print("--------------------------------------------------------------------------------------------------------")
    div_tag = soup.find_all("div")
    print ("number of a_tag is: ",len(div_tag))
    print("--------------------------------------------------------------------------------------------------------")
    print("downloading image (name will be logo.jpg)")
    sleep(1.5)
        



def directorio():
    url = "https://www.ufm.edu/Directorio"
    html_doc = requests.get(url)
    # THIS CREATES THE SOUP OBJECT
    soup = BeautifulSoup(html_doc.text,'html.parser')
    a_tag = soup.find_all("a",)
    emails = []
    cont = 0
    for i in a_tag:
        result = i.text.endswith("@ufm.edu")
        if result == True:
            emails.append(i.text)
            
    emails = list(dict.fromkeys(emails))
    emails.sort()
    f = open("directorio_emails","w+")
    f.write("emails are: ")
    f.write('\n')
    for i in emails:
        result_vocala = i.startswith("a")
        result_vocale = i.startswith("e")
        result_vocali = i.startswith("i")
        result_vocalo = i.startswith("o")
        result_vocalu = i.startswith("u")

        if result_vocala == True:
            cont = cont +1
        if result_vocale == True:
            cont = cont +1
        if result_vocalo == True:
            cont = cont +1
        if result_vocali == True:
            cont = cont +1
        if result_vocalu == True:
            cont = cont +1
        f.write("---------------------")
        f.write('\n')
        f.write(i)
        f.write('\n')
    print("====================================================================================================================")
    print("4.directorio")
    print("--------------------------------------------------------------------------------------------------------")
    print("imprimiendo directorio de emails a 4directorio_emails.txt")
    print("--------------------------------------------------------------------------------------------------------")