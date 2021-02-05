#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import os
os.system('clear')

class Dados_Caminho_Arquivos:
    def __init__(self, access_log='no_route'):
        self.caminho_access_log = access_log

    def confirma_caminho(self, decisao):
        if decisao == "n":
            self.caminho_access_log = input(
                "Digite o caminho correto do arquivo access.log |ex: /var/log/access.log|:")
        elif decisao == "y":
            pass


