# -*- coding: utf-8 -*-
import os
from Trie1 import Trie
from Trie1 import Element
from graph import Graph
from parser2 import Parser

class Ucitavanje(object):

    def __init__(self):
        self.trie = Trie(Element("KOREN",None))
        self.parser = Parser()
    def ucitavanje_sadrzaja_fajla(self,putanja):
        sadrzaj_foldera = []
        try:
            sadrzaj_foldera = os.listdir(putanja)
        except Exception:
            pass
        if len(sadrzaj_foldera) == 0:
            return False

def obilazak_stabla_direktorijuma(path):
    parser=Parser()
    for dic in os.listdir(path): #ovde imas samo ime
        dic=os.path.join(path,dic) #ovde mu dajes apsolutnu adresu
        if os.path.isdir(dic):
            obilazak_stabla_direktorijuma(dic)
        elif os.path.isfile(dic):
            #proveri da li je html
            #napraviti ubacivanje u graf i u stablo
            #fixme
            #for link in links ubaci
            links, words = parser.parse(dic)
            print(links)
            print(words)

def izbor():
    running=1
    obilazak_stabla_direktorijuma("python-2.7.7-docs-html\\c-api")

    while running==1:
        print("1-Prikazi trenutni direktorijum")
        print("2-Promeni direktorijum") #unesi apsolutnu putanju
        print("3-Unesi upit")
        print("0-Kraj programa")

        user_input=int(input(">>"))

        if user_input==1:
            print("--"*20)
            print("Trenutni direktorijum:\n{}".format(path))
            print("--"*20)
        elif user_input==2:
            new_path=os.path.abspath(input("Unesite putanju direktorijuma: "))
            print("--"*20)
            if os.path.exists(new_path) and os.path.isdir(new_path):
                path=new_path
                os.chdir(path)
                print("Uspesna promena direktorijuma!")
                print("Trenutni direktorijum:\n{}".format(path))
                obilazak_stabla_direktorijuma(path)
            else:
                print("Pogresan unos!")
                print("Trenutni direktorijum:\n{}".format(path))
                print("--"*20)
        elif user_input==0:
            print("Kraj!")
            return

if __name__ == '__main__':
    print('\nUcitavanje podataka u toku ...')
    izbor()
