import sys
import time
import colorama
import subprocess
import requests
import readline
from colorama import Fore
#Funciones argparse

class Decores:
    ban_a = ['cat', './banner/ban_A']

def funtion_basic_banner():
    subprocess.run(Decores.ban_a)
    print("Encuentra directorios escondidos")

def funtion_version():
    try:
        print("HiddenFind version 1.0 | First Version")
    except OSError:
        print("error al obtener la version")

def caterer():
    try:
        print("Directorios encontrados \n")
        subprocess.run(['cat', './log.txt'])
        subprocess.run(['rm', '-rf', './log.txt'])
        print("")
        print("\nProceso Cerrado")
    except OSError:
        print("Error al obtener el listado de logs")

def reader(rute, url):
    try:
        archivo = open(f'{rute}', 'r')
        main_read = archivo.readlines()
        #print(main_read)
        subprocess.run(Decores.ban_a)
        print(url+'SEARCH')
        print("Esto durara dependiendo del tamaño del wordlist \n Ve y tomate un cafe mientras ;)")
        print("Directorios encontrados[*]\n")
        print("=======Verificando directorios de wordlist")
        for x in main_read:
            more = x.strip()
            res = requests.get(url+more)
            #time.sleep(0.1)
            if(res.status_code != 404):
                print(f"True <---> {more} - response -> {res.status_code}")
                
                filer = open('./log.txt', 'a')
                filer.write(f'\n url {url}{more}')
                filer.close()
                #subprocess.run(['cat', './log.txt'])
            else:
                print(f"None <---> {more} - response -> {res.status_code}")
                #subprocess.run(['clear'])
                time.sleep(0.3)
        print("\n[*]Se encontraron los siguientes directorios")
        print("")
        subprocess.run(['cat', './log.txt'])
        subprocess.run(['rm', '-rf', './log.txt'])
        print("")
        print("\nProceso finalizado")
        
    except OSError:
        print("Error de conexion o error al cargar wordlists")
def funtion_wordlist_a(name, ptth):
    try:
        les = []
        for des in sys.argv[1]:
            les.append(des)
        #print(les)
        verificador = les[0]+les[1]+les[2]+les[3]+les[4]
        verificador_b = les[0]+les[1]+les[2]+les[3]
        if(verificador == 'https' or verificador_b == 'http'):
            reader(name, ptth)
        else:
            print("La url no es valida")
            
    except OSError:
        print("Error inesperado :(")
def funtion_manual():
    print("""
         Manual:
         Su uso basico es el siguiente.
         No olvides colocar una barra al final de la url
         python3 setup.py http://192.1.1.1/ -w /ruta/wordlist
         El programa hara una busqueda de directorios los
         resultados se te daran al finalizar.
         Puedes ver este manual con --help
         Puedes ver la version de la herramienta con --version
        """)
    sys.exit()
def funtion_default():
    print("Use --help")
    sys.exit()

if len(sys.argv) == 2:
    if(sys.argv[1] == "--help"):
        funtion_manual()
    else:   
        if(sys.argv[1] == "--version"):
            funtion_version()
elif len(sys.argv) > 2:
    print("Use --help")
    #funtion_default()
else:
    print("Porfavor escribe argumentos validos \n use --help")
if len(sys.argv) == 3 or 4:
    if(sys.argv[2] == "-w"):
        funtion_wordlist_a(sys.argv[3], sys.argv[1])
    else:
        print("Argumento no encontrado")
else:
    print("Porfavor escribe argumentos validos \n use --help")
    sys.exit()
