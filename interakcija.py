import os

from Trie_Proba import Trie, Element
from parser2 import Parser
from print_res import prikaz
from rang import rang
from set import operation_and, operation_or, operation_not
from sort import heap_sort
from stablo import kreiraj_graf, obilazak_stabla_direktorijuma


def izbor():
    running=1
    parser=Parser()
    edge_list=list()
    trie = Trie(Element("KOREN",None))
    g=None
    while running==1:
        print("1-Izaberi direktorijum")
        print("2-Prikazi trenutni direktorijum")
        print("3-Promeni direktorijum") #unesi apsolutnu putanju
        print("4-Unesi upit")
        print("0-Kraj programa")

        try:
            user_input=int(input(">>"))
        except ValueError:
            print("Unesite broj 0-4 iz ponudjenog menija.\n")
            continue

        if user_input==1:
            path=input(">>")
            g=kreiraj_graf(path,parser,trie)
        elif user_input==2:
            print("--"*20)
            print("Trenutni direktorijum:\n{}".format(path))
            print("--"*20)
        elif user_input==3:
            new_path=os.path.abspath(input("Unesite putanju direktorijuma: "))
            print("--"*20)
            if os.path.exists(new_path) and os.path.isdir(new_path):
                path=new_path
                os.chdir(path)
                print("Uspesna promena direktorijuma!")
                print("Trenutni direktorijum:\n{}".format(path))
                obilazak_stabla_direktorijuma(path, parser, edge_list, trie)
            else:
                print("Pogresan unos!")
                print("Trenutni direktorijum:\n{}".format(path))
                print("--"*20)
        elif user_input == 4:

            unos = input("Unesite željeni upit:\n").lower()
            lista_reci = unos.split()

            if "and" in lista_reci:
                if len(lista_reci) == 3 and lista_reci[1] == "and":
                    recnik1 = trie.pretraga(lista_reci[0])
                    recnik2 = trie.pretraga(lista_reci[2])
                    res_and = operation_and(recnik1, recnik2)
                    rang(res_and, g)
                    res_sort = heap_sort(res_and)
                    prikaz(res_sort)
                else:
                    print("\nNiste dobro uneli upit.\n")
            elif "or" in lista_reci:
                if len(lista_reci) == 3 and lista_reci[1] == "or":
                    recnik1 = trie.pretraga(lista_reci[0])
                    recnik2 = trie.pretraga(lista_reci[2])
                    res_or = operation_or(recnik1, recnik2)
                    res_rang=rang(res_or,g)
                    res_sort=heap_sort(res_rang)
                    prikaz(res_sort)
                else:
                    print("\nNiste dobro uneli upit.\n")
            elif "not" in lista_reci:
                if len(lista_reci) == 2 and lista_reci[0] == "not":
                    pass
                elif len(lista_reci) == 3 and lista_reci[1] == "not":
                    recnik1 = trie.pretraga(lista_reci[0])
                    recnik2 = trie.pretraga(lista_reci[2])
                    res_not = operation_not(recnik1, recnik2)
                    res_rang = rang(res_not, g)
                    res_sort = heap_sort(res_rang)
                    prikaz(res_sort)
                else:
                    print("\nNiste dobro uneli upit.\n")

            elif len(lista_reci) > 0:
                recnik1 = trie.pretraga(lista_reci[0])
                i = 1
                while i < len(lista_reci):
                    recnik2 = trie.pretraga(lista_reci[i])
                    recnik1 = operation_or(recnik1, recnik2)
                    i += 1
                if recnik1 == False:
                    print("Nema rezultata pretrage")
                else:
                    rang(recnik1, g)
                    res_sort = heap_sort(recnik1)
                    prikaz(res_sort)
            else:
                print("Niste uneli reci za pretragu.")
        elif user_input == 0:
            print("Kraj!")
            return
        else:
            print("Unesite broj 0-4 iz ponudjenog menija.")
