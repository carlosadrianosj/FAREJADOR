#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import time, sys, os
os.system('clear')

print('''
\n\n\n
  █████▒▄▄▄       ██▀███  ▓█████ ▄▄▄██▀▀▀▄▄▄      ▓█████▄  ▒█████   ██▀███  
▓██   ▒▒████▄    ▓██ ▒ ██▒▓█   ▀   ▒██  ▒████▄    ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒
▒████ ░▒██  ▀█▄  ▓██ ░▄█ ▒▒███     ░██  ▒██  ▀█▄  ░██   █▌▒██░  ██▒▓██ ░▄█ ▒
░▓█▒  ░░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄▓██▄██▓ ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░▒██▀▀█▄  
░▒█░    ▓█   ▓██▒░██▓ ▒██▒░▒████▒▓███▒   ▓█   ▓██▒░▒████▓ ░ ████▓▒░░██▓ ▒██▒
 ▒ ░    ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░▒▓▒▒░   ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░       ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░▒ ░▒░    ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░
 ░ ░     ░   ▒     ░░   ░    ░   ░ ░ ░    ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░░   ░ 
             ░  ░   ░        ░  ░░   ░        ░  ░   ░        ░ ░     ░     
                                                   ░                        
                       (programador: carlosadrianosj)
          (Ferramenta criada para investigação em arquivo access.log)
                         (Para opções, digite help)
\n\n\n\
''')

#verifica se o programa foi executado em modo root
root = os.geteuid()
if root == 1000:
      print("              Este programa precisa ser executado em modo ROOT!!")
      time.sleep(0.5)
      print("              Este programa precisa ser executado em modo ROOT!!")
      time.sleep(0.5)
      print("              Este programa precisa ser executado em modo ROOT!!")
      time.sleep(0.5)
      print("                  Exemplo: sudo python3 farejador.py\n\n\n\n")
      time.sleep(0.5)
      os._exit()
elif root == 0:
      pass


caminho_do_arquivo = input("Digite o caminho do arquivo access.log |ex: /var/log/access.log|:")
certeza = input("\n\nEste caminho é o correto |y/n|? ")
if certeza == "n":
    caminho_do_arquivo = input("\n\nDigite o caminho correto do arquivo access.log |ex: /var/log/access.log|:\n\n")
elif certeza == "y":
    pass
print("\n\n")
comando = True

while comando:
    
    #captura a opção digitada pelo usuário
    comando = str(input("FAREJADOR> ")) 

    #compara a variável comando com as opções existentes no programa
    if comando == "help": 
        print('''
       
                               __COMANDOS__ 

    req = irá exibir as requisições feitas por um IP específico                                                                
    enum = enumera os IP's do arquivo por ordem de acesso (ajuda a reconhecer o IP malicioso)                                       
    tempo = determina o horario de inicio e de termino de acesso do IP especificado                                                 
    procura = procura entre os logs o que o usuário digitou
    exit = fecha o programa   
            
            ''')

    elif comando == "enum":
        print("\n\n#############_Enumeração_##############\n\n")
        os.system('sudo cat {} | cut -d " " -f 1 | sort | uniq -c | sort -unr'.format(caminho_do_arquivo))
        print("\n\n#######################################\n\n")  
      

    elif comando == "tempo":
        ip = input("Digite aqui o IP que será analizado|ex: 192.168.0.7|: ")
        print("\n\n#############_Horario_de_Inicio_##############\n\n")
        os.system('sudo cat {} | grep "{}" | head -n1'.format(caminho_do_arquivo, ip))
        print("\n\n##############################################\n\n") 
        print("#############_Horario_de_Termino_#############\n\n")
        os.system('sudo cat {} | grep "{}" | tail -n1'.format(caminho_do_arquivo, ip))
        print("\n\n##############################################\n\n")

    elif comando == "procura":
        ip = input("Digite aqui o IP que será analizado|ex: 192.168.0.7|: ")
        print('''\n\n
        #########################
        # Exemplos de pesquisa: #
        # * Nmap                #
        # * Nikto               #
        # * Nessus              #
        #########################
        ''')
        procura = input("\n\nDigite o que deseja procurar: ")    
        print("\n\n##############_Procura_################\n\n")
        os.system('sudo cat {} | grep "{}" | grep "{}"'.format(caminho_do_arquivo, ip, procura))
        print("\n\n#######################################\n\n")

    elif comando == "req":
        ip = input("Digite aqui o IP que será analizado|ex: 192.168.0.7|: ")
        print('''\n\n
        ###########################################
        # Pesquisa de requisição por status code: #
        # * 200                                   #
        # * 301                                   #
        # * 404                                   #
        ###########################################
        ''')
        requisicao = input("\n\nDigite o status code que deseja procurar: ")
        if requisicao == "200":
            print("\n\n################_Requisições_200_###################\n\n")
            os.system('sudo cat {} | grep "{}" | cut -d "]" -f2 |  grep "{}"'.format(caminho_do_arquivo, ip, requisicao))
            print("\n\n####################################################\n\n")           

        elif requisicao == "301":
            print("\n\n################_Requisições_301_###################\n\n")
            os.system('sudo cat {} | grep "{}" | cut -d "]" -f2 |  grep "{}"'.format(caminho_do_arquivo, ip, requisicao))
            print("\n\n####################################################\n\n") 

        elif requisicao == "404":
            print("\n\n################_Requisições_404_###################\n\n")
            os.system('sudo cat {} | grep "{}" | cut -d "]" -f2 |  grep "{}"'.format(caminho_do_arquivo, ip, requisicao))
            print("\n\n####################################################\n\n") 

    elif comando == "exit":
        print("Volte Sempre")
        time.sleep(2)
        break
        

 