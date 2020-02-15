import os

from graph import Graph
from parser2 import Parser
from Trie1 import Trie,Element
from set import operation_and,operation_not,operation_or

def obilazak_stabla_direktorijuma(path, parser ,edge_list,trie):
    parser=Parser()
    for dic in os.listdir(path): #ovde imas samo ime
        dic=os.path.join(path,dic) #ovde mu dajes apsolutnu adresu
        if os.path.isdir(dic):
            obilazak_stabla_direktorijuma(dic,parser,edge_list,trie)
        elif os.path.isfile(dic):
            if ".html" in dic:
                links, words = parser.parse(dic)
                #print(links)
                for rec in words:
                    trie.dodaj_rec(rec.lower(),dic)
                for link in links:
                    edge_list.append((dic,link))
    # print(links)
    #print(words)

def kreiraj_graf(path,parser,trie):
    print('\nUcitavanje podataka u toku ...')

    edge_list=list()
    graph=Graph()
    obilazak_stabla_direktorijuma(path,parser,edge_list,trie)

    V=set()
    for e in edge_list:
        V.add(e[0])
        V.add(e[1])

    verts={}

    for v in V:
        verts[v]=graph.insert_vertex(v)

    for e in edge_list:
        src=e[0]
        dest=e[1]

        graph.insert_edge(verts[src], verts[dest])

    return graph

def izbor():
    running=1
    parser=Parser()
    edge_list=list()
    trie = Trie(Element("KOREN",None))

    while running==1:
        print("1-Izaberi direktorijum")
        print("2-Prikazi trenutni direktorijum")
        print("3-Promeni direktorijum") #unesi apsolutnu putanju
        print("4-Unesi upit")
        print("0-Kraj programa")

        user_input=int(input(">>"))

        if user_input==1:
            path=input(">>")
            kreiraj_graf(path,parser,trie)

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
                obilazak_stabla_direktorijuma(path)
            else:
                print("Pogresan unos!")
                print("Trenutni direktorijum:\n{}".format(path))
                print("--"*20)
        elif user_input == 4:

            unos = input("Unesite željeni upit:\n").lower()
            lista_reci = unos.split()

            if ('and' or 'not' or 'or') not in lista_reci:
                for i in range(len(lista_reci)):
                    trie.pretraga(lista_reci[i])
                # pozivam ovde or funkciju
            else:
                if "and" in lista_reci:
                    if len(lista_reci) == 3 and lista_reci[1] == "and":
                        recnik1 = trie.pretraga(lista_reci[0])
                        recnik2 = trie.pretraga(lista_reci[2])
                        rezultat_and = operation_and(recnik1,recnik2)
                        return print(rezultat_and)
                elif "or" in lista_reci:
                    if len(lista_reci) == 3 and lista_reci[1] == "or":
                        recnik1 = trie.pretraga(lista_reci[0])
                        recnik2 = trie.pretraga(lista_reci[2])
                        rezultat_or = operation_or(recnik1, recnik2)
                        return rezultat_or
                elif "not" in lista_reci:
                    if len(lista_reci) == 2 and lista_reci[0] == "not":
                        pass
                    elif len(lista_reci) == 3 and lista_reci[1] == "not":
                        recnik1 = trie.pretraga(lista_reci[0])
                        recnik2 = trie.pretraga(lista_reci[2])
                        rezultat_not = operation_not(recnik1, recnik2)
                        return rezultat_not
                else:
                    print("\nNiste dobro uneli upit.\n")
        elif user_input == 0:
            print("Kraj!")
            return