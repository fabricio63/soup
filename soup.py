import requests
from bs4 import BeautifulSoup
from sys import argv
import code
def all():
    code.portal()
    print("")
    print("")
    print("")
    code.estudio()
    print("")
    print("")
    print("")
    code.css()
    print("")
    print("")
    print("")
    code.directorio()

def main():
    arg = len(argv)
    try:
        if arg == 1:
            all()
        elif arg !=1:
            if argv[1] =='1':
                code.portal()
            if argv[1] == '2':
                code.estudio() 
            if argv[1] == '3':
                code.css()
            if argv[1] == '4':
                code.directorio()
    except:
        print("command line argument not valid")

main()
            



