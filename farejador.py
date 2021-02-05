#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import os
import time

from packet.Class_Farejador import Farejador
from packet.Class_Utils import Utils
from packet.Class_Dados_Caminho_Arquivos import Dados_Caminho_Arquivos
farejador = Farejador()
utils = Utils()
dados = Dados_Caminho_Arquivos()
os.system('clear')

utils.root()
print(utils.get_banner())
time.sleep(2)

caminho_do_arquivo = input("\n\ndigite aqui o caminho do arquivo |ex: /var/log/access.log|: ")
direcao = Dados_Caminho_Arquivos(caminho_do_arquivo)
confirma = input("Este é o caminho correto(y/n)? ")
direcao.confirma_caminho(confirma)

# compara a variável comando com as opções existentes no programa
while True:
    comando = str(input("FAREJADOR> "))

    if comando == "help":
        print(utils.get_menu())

    elif comando == "enum":
        farejador.enumeracao(direcao.caminho_access_log)

    elif comando == "tempo":
        farejador.tempo(direcao.caminho_access_log)

    elif comando == "procura":
        farejador.procura(direcao.caminho_access_log)

    elif comando == "req":
        farejador.requisicao(direcao.caminho_access_log)

    elif comando == "exit":
        utils.exit()
