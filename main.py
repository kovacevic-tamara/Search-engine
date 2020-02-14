# -*- coding: utf-8 -*-
import os
from Trie1 import Trie
from Trie1 import Element
from graph import Graph
from parser2 import Parser
from set import operation_and, operation_or, operation_not
from stablo import izbor, kreiraj_graf


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

if __name__ == '__main__':
    izbor()
  # lista1={'dd.html':2,'bb.html':3}
   #lista2={'aa.html':3,'bb.html':1,'cc.html':6}
   #print(operation_not(lista1,lista2))

