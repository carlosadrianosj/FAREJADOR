#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import os
import time
from Class_Utils import Utils
from Class_Dados_Caminho_Arquivos import Dados_Caminho_Arquivos
from Class_Farejador import Farejador
os.system('clear')

utils = Utils()
dados = Dados_Caminho_Arquivos()
farejador = Farejador()
utils.root()
print(utils.get_banner())
time.sleep(2)

caminho_do_arquivo = input("\n\ndigite aqui o caminho do arquivo |ex: /var/log/access.log|: ")
dados = Dados_Caminho_Arquivos(caminho_do_arquivo)
confirma = input("Este é o caminho correto(y/n)? ")
dados.confirma_caminho(confirma)

# compara a variável comando com as opções existentes no programa
while True:
    comando = str(input("FAREJADOR> "))

    if comando == "help":
        print(utils.get_menu())

    elif comando == "enum":
        farejador.enumeracao(dados.caminho_access_log)

    elif comando == "tempo":
        farejador.tempo(dados.caminho_access_log)

    elif comando == "procura":
        farejador.procura(dados.caminho_access_log)

    elif comando == "req":
        farejador.requisicao(dados.caminho_access_log)

    elif comando == "exit":
        utils.exit()


