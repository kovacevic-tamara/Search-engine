import os

from Trie_Proba import Trie, Element
from parser2 import Parser
from print_res import prikaz
from rang import rang
from set import Set
from sort import heap_sort
from stablo import kreiraj_graf



#fixme sta raditi sa klasom set ne radi kad se pozove resSet vec samo Set
def izbor():
    running=1
    parser=Parser()
    trie = Trie(Element("KOREN",None))
    g=None
    path=str()
    resSet=Set()
    flag = True
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
            if flag and len(path)!=0:
                print("Za promenu direktorijuma izaberite opciju 3!\n")
                continue
            path = input(">>")
            g=kreiraj_graf(path,parser,trie)
            if g == False:
                print("Niste dobro uneli putanju direktorijuma\n")
                flag = False
            else:
                flag = True

        elif user_input==2:
            if not flag or len(path)==0:
                print("Neophodno je izabrati direktorijum!\n")
                continue
            print("Trenutni direktorijum:\n{}".format(path))
            print("-"* len(path))
        elif user_input==3:
            if len(path)==0 or not flag:
                print("Trenutno niste pozicionirani ni na jednom direktorijumu!\n")
                continue
           # new_path=os.path.abspath(input("Unesite putanju direktorijuma: ")) #fixme zbog linuxa
            new_path=input("Unesite putanju direktorijuma: ")
            if os.path.exists(new_path) and os.path.isdir(new_path) and new_path!=path:
                path=new_path
               # os.chdir(new_path)
                print("Uspesna promena direktorijuma!")
                trie = Trie(Element("KOREN",None))
                g = kreiraj_graf(path, parser, trie)
                #fixme puca kad se unese upit nakon promene direktorijumaaaaaaaaaaaa proveriti!
            else:
                print("Pogresan unos!")
                print("Trenutni direktorijum:\n{}".format(path))
                print("--"*20)
        elif user_input == 4:
            if len(path)==0 or not flag:
                print("Trenutno niste pozicionirani ni na jednom direktorijumu!\n")
                continue
            else:
                unos = input("Unesite željeni upit:\n").lower()
                lista_reci = unos.split()

                if "and" in lista_reci:
                    if len(lista_reci) == 3 and lista_reci[1] == "and":
                        if lista_reci[0].lower() != lista_reci[2].lower():
                            recnik1 = trie.pretraga(lista_reci[0])
                            recnik2 = trie.pretraga(lista_reci[2])
                            res_and = Set.operation_and(recnik1, recnik2)
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
                            res_or = Set.operation_or(recnik1, recnik2)
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
                            res_not = Set.operation_not(recnik1, recnik2)
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
                            recnik1 = Set.operation_or(recnik1, recnik2)
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
            print("Kraj!")
            return
        else:
            print("Unesite broj 0-4 iz ponudjenog menija.")
