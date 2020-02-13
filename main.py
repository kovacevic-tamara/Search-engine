# -*- coding: utf-8 -*-
import os
from Trie1 import Trie
from Trie1 import Element
from graph import Graph
from parser2 import Parser
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
