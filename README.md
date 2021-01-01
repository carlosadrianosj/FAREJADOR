# FAREJADOR
Este projeto teve como intuito desenvolver um programa que auxiliasse administradores de rede a investigar requisições maliciosas por meio de pesquisas no access.log!

Totalmente construido em Python, o Farejador faz pesquisas pré-determinadas no arquivo access.log, a atual 
versão da ferramenta possui as seguintes opções:

                               __COMANDOS__ 

    req = irá exibir as requisições feitas por um IP específico                                                                
    enum = enumera os IP's do arquivo por ordem de acesso (ajuda a reconhecer o IP malicioso)                                       
    tempo = determina o horario de inicio e de termino de acesso do IP especificado                                                 
    procura = procura entre os logs o que o usuário digitou                            
    exit = fecha o programa 

requisitos:
* sudo apt install python
* sudo apt install python3

para executar o programa: 
* sudo python3 farejador.py
