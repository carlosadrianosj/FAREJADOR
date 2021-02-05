#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import time
import sys
import os
os.system('clear')

class Utils:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.menu = os.path.join(self.base_dir, 'menu.txt')
        self.banner = os.path.join(self.base_dir, 'banner.txt')

    def get_banner(self):
        os.system('clear')
        with open(self.banner, 'r') as banner:
            return '\033[35m'+ banner.read()

    def get_menu(self):
        os.system('clear')
        with open(self.menu, 'r') as menu:
            return '\033[35m'+ menu.read()

    def root(self):
        permissao_do_usuario = os.geteuid()
        if permissao_do_usuario != 0:
            for i in range(5):
                print("\033[93m              Este programa precisa ser executado em modo ROOT!!\n\n")
                time.sleep(0.5)
            print("\033[93m                      Exemplo: sudo python3 farejador.py")
            time.sleep(2)
            os.system('clear')
            sys.exit(0)
        else:
            pass

    def exit(self):
        print("Volte Sempre")
        time.sleep(2)
        os.system('clear')
        sys.exit()


class Dados_Caminho_Arquivos:
    def __init__(self, access_log='no_route'):
        self.caminho_access_log = access_log

    def confirma_caminho(self, decisao):
        if decisao == "n":
            self.caminho_access_log = input(
                "Digite o caminho correto do arquivo access.log |ex: /var/log/access.log|:")
        elif decisao == "y":
            pass


utils = Utils()
dados = Dados_Caminho_Arquivos()
farejador = Farejador()
utils.root()
print(utils.get_banner())
#time.sleep(2)

caminho_do_arquivo = input("\n\ndigite aqui o caminho do arquivo |ex: /var/log/access.log|: ")
dados = Dados_Caminho_Arquivos(caminho_do_arquivo)
confirma = input("Este é o caminho correto(y/n)? ")
dados.confirma_caminho(confirma)
print(dados.caminho_access_log)


while True:
    comando = str(input("FAREJADOR> "))

    # compara a variável comando com as opções existentes no programa
    if comando == "help":
        print(utils.get_menu())

    elif comando == "enum":
        farejador.enumeracao()

    elif comando == "tempo":
        farejador.tempo()

    elif comando == "procura":
        farejador.procura()

    elif comando == "req":
        farejador.requisicao()

    elif comando == "exit":
        utils.exit()


