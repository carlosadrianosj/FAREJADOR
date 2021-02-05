#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import time
import sys
import os
os.system('clear')

class Utils:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.menu = os.path.join(self.base_dir, '../menu.txt')
        self.banner = os.path.join(self.base_dir, '../banner.txt')

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
