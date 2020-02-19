import os

from graph import Graph
from parser2 import Parser
from Trie_Proba import Trie,Element
from rang import rang, prikaz, heap_sort
from set import resultSet

def obilazak_stabla_direktorijuma(path, parser ,edge_list,trie):
    parser=Parser()
    sadrzaj_foldera = []
    try:
        sadrzaj_foldera = os.listdir(path)
    except Exception:
        pass
    if len(sadrzaj_foldera) == 0:
        return False
    for dic in sadrzaj_foldera: #ovde imas samo ime
        dic = os.path.join(path,dic) #ovde mu dajes apsolutnu adresu
        if os.path.isdir(dic):
            obilazak_stabla_direktorijuma(dic,parser,edge_list,trie)
        else:
            if dic.endswith(".html"):
                links, words = parser.parse(dic)
                #print(links)
                for rec in words:
                    rec = rec.lower()
                    #trie.dodaj_rec(rec,dic)

                    if rec in trie.recnik:
                        if dic not in trie.recnik[rec]:
                            trie.recnik[rec][dic] = 1
                        else:
                            trie.recnik[rec][dic] +=1;
                    else:
                        trie.dodaj_rec(rec,dic)
                for link in links:
                    edge_list.append((dic,link))

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

    #print(graph)
    return graph

def izbor():
    running=1
    parser=Parser()
    edge_list=list()
    trie = Trie(Element("KOREN",None))
    result_set=resultSet()

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
            print(trie.recnik['python'])
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
                if len(lista_reci) > 0:
                    recnik1 = trie.pretraga(lista_reci[0])
                    print(recnik1)
                    i = 1
                    while i < len(lista_reci):
                        recnik2 = trie.pretraga(lista_reci[i])
                        recnik1 = set.operation_or(recnik1,recnik2)
                        i+=1

                    if recnik1 == False:
                        print("Nema rezultata pretrage")
                    else:
                        print(recnik1)
                else:
                    print("Niste uneli reci za pretragu.")
            else:
                if "and" in lista_reci:
                    if len(lista_reci) == 3 and lista_reci[1] == "and":
                        recnik1 = trie.pretraga(lista_reci[0])
                        recnik2 = trie.pretraga(lista_reci[2])
                        rezultat_and = resultSet.operation_and(recnik1,recnik2)
                        #prikaz(rezultat_and)
                        rezultat_rang=rang(rezultat_and, g)
                        rezultat_sort=heap_sort(rezultat_rang)
                        #rezultat_sort=heap_sort(rezultat_and)
                        prikaz(rezultat_sort)
                        return rezultat_and

                elif "or" in lista_reci:
                    if len(lista_reci) == 3 and lista_reci[1] == "or":
                        recnik1 = trie.pretraga(lista_reci[0])
                        recnik2 = trie.pretraga(lista_reci[2])
                        rezultat_or = resultSet.operation_or(recnik1, recnik2)
                        #rezultat_rang=rang(rezultat_or,g)
                        #rezultat_sort=heap_sort(rezultat_rang)
                        #prikaz(rezultat_sort)
                elif "not" in lista_reci:
                    if len(lista_reci) == 2 and lista_reci[0] == "not":
                        pass
                    elif len(lista_reci) == 3 and lista_reci[1] == "not":

                        recnik1 = trie.pretraga(lista_reci[0])
                        recnik2 = trie.pretraga(lista_reci[2])
                        rezultat_not = resultSet.operation_not(recnik1, recnik2)
                        #rezultat_rang = rang(rezultat_not, g)
                        #rezultat_sort = heap_sort(rezultat_rang)
                        #prikaz(rezultat_sort)
                else:
                    print("\nNiste dobro uneli upit.\n")
        elif user_input == 0:
            print("Kraj!")
            return
        else:
            print("Unesite broj 0-4 iz ponudjenog menija.")
