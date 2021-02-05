#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import os
os.system('clear')

class Farejador:
    def __init__(self):
        pass

    def enumeracao(self, caminho):
        print("\n\n#############_Enumeração_##############\n\n")
        os.system('sudo cat {} | cut -d " " -f 1 | sort | uniq -c | sort -unr'.format(caminho))
        print("\n\n#######################################\n\n")

    def tempo(self, caminho):
        ip = input("Digite aqui o IP que será analizado|ex: 192.168.0.7|: ")
        print("\n\n#############_Horario_de_Inicio_##############\n\n")
        os.system('sudo cat {} | grep "{}" | head -n1'.format(caminho, ip))
        print("\n\n##############################################\n\n")
        print("#############_Horario_de_Termino_#############\n\n")
        os.system('sudo cat {} | grep "{}" | tail -n1'.format(caminho, ip))
        print("\n\n##############################################\n\n")

    def procura(self, caminho):
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
        os.system('sudo cat {} | grep "{}" | grep "{}"'.format(caminho, ip, procura))
        print("\n\n#######################################\n\n")

    def requisicao(self, caminho):
        ip = input("Digite aqui o IP que será analizado|ex: 192.168.0.7|: ")
        print('''\n\n
                ###########################################
                # Pesquisa de requisição por status code: #
                # * 200                                   #
                # * 301                                   #
                # * 404                                   #
                ###########################################
                ''')
        req = input("\n\nDigite o status code que deseja procurar: ")
        if req == "200":
            print("\n\n################_Requisições_200_###################\n\n")
            os.system(
                'sudo cat {} | grep "{}" | cut -d "]" -f2 |  grep "{}"'.format(caminho, ip, req))
            print("\n\n####################################################\n\n")

        elif req == "301":
            print("\n\n################_Requisições_301_###################\n\n")
            os.system(
                'sudo cat {} | grep "{}" | cut -d "]" -f2 |  grep "{}"'.format(caminho, ip, req))
            print("\n\n####################################################\n\n")

        elif req == "404":
            print("\n\n################_Requisições_404_###################\n\n")
            os.system(
                'sudo cat {} | grep "{}" | cut -d "]" -f2 |  grep "{}"'.format(caminho, ip, req))
            print("\n\n####################################################\n\n")

