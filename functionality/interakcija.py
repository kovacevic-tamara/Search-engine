import os

from structures.Trie_Proba import Trie, Element
from parser2 import Parser
from functionality.print_res import prikaz
from functionality.rang import rang
from structures.set import Set
from functionality.sort import heap_sort
from functionality.stablo import kreiraj_graf

def izbor():
    running=1
    parser=Parser()
    trie = Trie(Element("KOREN",None))
    g=None
    path=str()
    resSet=Set()
    while running==1:
        print("(1)->Izbor direktorijuma")
        print("(2)->Prikaz trenutnog direktorijuma")
        print("(3)->Promena direktorijuma") #unesi apsolutnu putanju
        print("(4)->Unos upita")
        print("(0)->Kraj programa")

        try:
            user_input=int(input(">>"))
        except ValueError:
            print("Unesite broj 0-4 iz ponudjenog menija.\n")
            continue

        if user_input==1:
            if len(path)!=0:
                print("Za promenu direktorijuma izaberite opciju 3!\n")
                continue
            path=os.path.abspath(input("Unesite apsolutnu/relativnu putanju do željenog direktorijuma >> "))
            g=kreiraj_graf(path,parser,trie)
        elif user_input==2:
            if len(path)==0:
                print("Neophodno je izabrati direktorijum!\n")
                continue
            print("Trenutni direktorijum:\n{}".format(path))
            print("-"* len(path))
        elif user_input==3:
            if len(path)==0:
                print("Trenutno niste pozicionirani ni na jednom direktorijumu!\n")
                continue
            new_path=os.path.abspath(input("Unesite putanju direktorijuma: "))
            #new_path=input("Unesite putanju direktorijuma: ")
            if os.path.exists(new_path) and os.path.isdir(new_path) and new_path!=path:
                path=new_path
                os.chdir(new_path)
                print("Uspesna promena direktorijuma!")
                trie = Trie(Element("KOREN",None))
                g = kreiraj_graf(path, parser, trie)
            else:
                print("Pogrešan unos!")
                print("Trenutni direktorijum:\n{}".format(path))
                print("--"*20)
        elif user_input == 4:
            unos = input("Unesite željeni upit:\n").lower()
            lista_reci = unos.split()

            if "and" in lista_reci:
                if len(lista_reci) == 3 and lista_reci[1] == "and":

                    if lista_reci[0].lower() != lista_reci[2].lower():
                        recnik1 = trie.pretraga(lista_reci[0])
                        recnik2 = trie.pretraga(lista_reci[2])
                        res_and = resSet.operation_and(recnik1, recnik2)
                        rang(res_and, g)
                        res_sort = heap_sort(res_and)
                        prikaz(res_sort)
                    else:
                        print("\nUneli ste dve iste reci. Upit nije validan.\n")
                else:
                    print("\nNiste dobro uneli upit.\n")
            elif "or" in lista_reci:
                if len(lista_reci) == 3 and lista_reci[1] == "or":
                    if lista_reci[0].lower() != lista_reci[2].lower():
                        recnik1 = trie.pretraga(lista_reci[0])
                        recnik2 = trie.pretraga(lista_reci[2])
                        res_or = resSet.operation_or(recnik1, recnik2)
                        res_rang=rang(res_or,g)
                        res_sort=heap_sort(res_rang)
                        prikaz(res_sort)
                    else:
                        print("\nUneli ste dve iste reci. Upit nije validan.\n")
                else:
                    print("\nNiste dobro uneli upit.\n")
            elif "not" in lista_reci:
                if len(lista_reci) == 3 and lista_reci[1] == "not":
                    if lista_reci[0].lower() != lista_reci[2].lower():
                        recnik1 = trie.pretraga(lista_reci[0])
                        recnik2 = trie.pretraga(lista_reci[2])
                        res_not = resSet.operation_not(recnik1, recnik2)
                        res_rang = rang(res_not, g)
                        res_sort = heap_sort(res_rang)
                        prikaz(res_sort)
                    else:
                        print("\nUneli ste dve iste reci. Upit nije validan.\n")
                else:
                    print("\nNiste dobro uneli upit.\n")

            elif len(lista_reci) > 0:
                indikator = False
                for rec in lista_reci:
                    if lista_reci.count(rec) > 1:
                        indikator = True
                        break
                if indikator == False:
                    recnik1 = trie.pretraga(lista_reci[0])
                    i = 1
                    while i < len(lista_reci):

                        recnik2 = trie.pretraga(lista_reci[i])
                        recnik1 = resSet.operation_or(recnik1, recnik2)
                        i += 1
                    if recnik1 == False:
                        print("\nNema rezultata pretrage\n")
                    else:
                        rang(recnik1, g)
                        res_sort = heap_sort(recnik1)
                        prikaz(res_sort)
                else:
                    print("\nNiste dobro uneli upit, reci ne smeju da se ponavljaju.\n")
            else:
                print("\nNiste uneli reci za pretragu.\n")
        elif user_input == 0:
            print("Program završen!")
            return
        else:
            print("Unesite broj 0-4 iz ponudjenog menija.")
