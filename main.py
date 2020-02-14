# -*- coding: utf-8 -*-
import os
from Trie1 import Trie
from Trie1 import Element
from graph import Graph
from parser2 import Parser
from set import operation_and, operation_or, operation_not
from stablo import izbor, kreiraj_graf

if __name__ == '__main__':
   # izbor()
   lista1={'dd.html':2,'bb.html':3}
   lista2={'aa.html':3,'bb.html':1,'cc.html':6}
   print(operation_not(lista1,lista2))

