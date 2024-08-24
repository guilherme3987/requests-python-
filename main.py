import requests
import os
import art
import time

"""
Creating a txt file
 arquivo = open("subdominios.txt", "w")
 arquivo.write("login.php")
 arquivo.close()
"""

# functions for styles
def clean():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Unix
        os.system("clear")

def loading(segundos):
    for i in range(segundos):
        print("\033[91mLoading" + "." * i, end="\r\033[m")
        time.sleep(1)
    print("\033[91mReady !" + " " * len("Loading" + ".\033[m" * segundos))


def loading_exit(seconds):
  for i in range(seconds):
    print("\033[91mLoading" + "." * i, end="\r\033[m")
    time.sleep(1)
  print("\033[91mReady !" + " " * len("Loading" + ".\033[m" * seconds))


def menu():
  red = "\033[31m"
  reset = "\033[0m"
  my_logo = red + art.text2art("REQSCAN ") + reset
  print(my_logo)



  print("\033[36m\tProgram made by guizin_3987, a student of the Information Systems course at the State University of Bahia.\n\tThe code is made in Python and its libraries for HTTP/TCP request.\n\tATTENTION: CODE MADE FOR EDUCATIONAL PURPOSES, ANY IMPROPER USE THAT VIOLATES THE LAW IS THE RESPONSIBILITY OF THE USER.\033[0m")
  time.sleep(2)
  
  print(red + "\n\n*********************************************************\n\n\t------------- MENU --------------\n\n\t [0] -- Return all requests\n\n\t [1] -- Return requests with wordlist\n\n\t [2] -- Return server encoding (txt and binary)\n\n\t [3] -- Return headers\n\n\t [4] -- Help (pt or en)\n\n\t [5] -- Exit\n\n*********************************************************\n\n\t= "+reset)
  

menu() 






#Function for all requests
def requestsgenearl(url):

  r = requests.get(url)
  
  print("\033[1;38;2;255;165;0m\n\n\tStatus: \033[m")
  print("\n\t",r.status_code)
  if(r.status_code == 200):
    print("\033[1;32m\n\t SERVER IS WORKING\033[m")
  else:
    print("\033[31m\n\tSERVER IS NOT WORKINH [bad requests 4xxx or 5xxx]\033[m")

    
  time.sleep(2)
  print("\033[32m\n\n\n\tServers answers\n\t\033[0;0m")
  print(r.text)
  time.sleep(2)
  print("\033[32m\n\n\n\tHeaders HTTP\n\t\033[0;0m")
  print(r.encoding) 
  time.sleep(2)
  print("\033[32m\n\n\n\tBytes answers\n\t\033[0;0m")
  print(r.content)
  time.sleep(2)
  print("\033[32m\n\n\n\tRequests headers\n\t\033[0;0m")
  print(r.headers)
  time.sleep(2)
  print("\033[32m\n\n\n\tDelta time\n\t\033[0;0m")
  print(r.elapsed)


# function for wrodlists
def check_subdomains(url):
    with open('subdominios.txt', 'r') as arquivo:
        for linha in arquivo:
            palavra = linha.strip()
            nova_url = url + palavra
            resposta = requests.get(nova_url)
            if(resposta.status_code == 200):
                print(nova_url)
                print("\033[1;32m\n\t SERVER IS WORKING\033[m",resposta)
                time.sleep(2)
                print("\n\nServer Answers\n\n",resposta.text)
                print("\n\n\n")
            else: 
                print(nova_url)
                time.sleep(2)
                print("\033[1;31m\n\tSERVER IS NOT WORKING OR DONT EXIST [bad requests 4xxx or 5xxx]\033[m")



              
# fuction for encoding
def requestsencoding(url):
   r = requests.get(url)
   time.sleep(2)
   print("\n\n\n\tServers answers\n\n\n")
   print("\n",r.text)
   time.sleep(2)
   print("\n\n\n\tBytes answers\n\t")
   print("\n",r.content)

def requestsheaders(url):
  r = requests.get(url)
  time.sleep(2)
  print("\n\n\n\tHeaders\n\t")
  time.sleep(2)
  print("\n",r.headers)


choice = int(input())

while choice not in [0,1,2,3,4]:
  print("Invalid choice\n\tChoice = ")
  choice = int(input())


# requestsgenearl
while choice == 0:
  loading(5)
  time.sleep(2)
  clean()
  url = input("\n\n\n\tURL for HTTP/TCP requests [http://example.com/]:  ")
  requestsgenearl(url)
  time.sleep(2)
  print("\n\n\n\n")
  time.sleep(2)
  menu()
  choice = int(input())


# check_subdomains
while choice == 1:
  loading(5)
  clean()
  url = input("\n\n\n\tURL for HTTP/TCP requests [http://example.com/]:  ")
  check_subdomains(url)
  time.sleep(2)
  print("\n\n\n\n")
  time.sleep(2)
  menu()
  choice = int(input())

  
# requestsencoding
while choice ==2:
  loading(5)
  clean()
  url = input("\n\n\n\tURL for HTTP/TCP requests [http://example.com/]:  ")
  requestsencoding(url)
  time.sleep(2)
  print("\n\n\n")
  time.sleep(2)
  menu()
  choice = int(input())


# requestsheaders
while choice ==3:
  loading(5)
  clean()
  url = input("\n\n\n\tURL for HTTP/TCP requests [http://example.com/]:  ")
  requestsheaders(url)
  time.sleep(2)
  print("\n\n\n")
  time.sleep(2)
  menu()
  choice = int(input())


# help
while choice == 4:
  loading(5)
  clean()
  print("\n\tpt -- 1\n\ten -- 2\n=> ")
  choice_2 = int(input())
  
  if choice_2 == 1:
    print("\033[43m\n\nPara problemas com a biblioteca requests\n\n\tA biblioteca requests é uma biblioteca Python usada para enviar solicitações HTTP.Para usar a biblioteca requests, primeiro você precisa instalá-la. Você pode instalar a biblioteca requests usando o gerenciador de pacotes pip no seu terminal: pip install requests \n\tDepois de instalado reinicie seu compilador\n\nPara problemas com URLs\n\n\tA entrada de dados da URL deve ser desse tipo: http://exemplo.com/\033[m")
  
  if choice_2 == 2:
    print("\033[43m\n\nFor problems with libary requests\n\n\tThe requests library is a Python library used to send HTTP requests. To use the requests library, you first need to install it. You can install the requests library using the pip package manager in your terminal: pip install requests.Once installed, restart your compiler\n\nFor problems with URLs\n\n\tThe URL data entry should be of this type: http://example.com/\033[m")


  time.sleep(2)
  menu()
  choice = int(input()) 
  clean()

  

if(choice == 5):
  loading_exit(5)
  clean()
  os._exit(0)
  
  




