import os

from graph import Graph
from parser2 import Parser

def obilazak_stabla_direktorijuma(path, parser ,edge_list,trie):
    #parser=Parser()
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
    print('\nUcitavanje podataka u toku ...\n')

    edge_list=list()
    graph=Graph()

    obilazak_stabla_direktorijuma(path,parser,edge_list,trie)
    V=set()

    for e in edge_list:
        V.add(e[0])
        V.add(e[1])

    for v in V:
       graph.insert_vertex(v)

    for e in edge_list:
        src=e[0]
        dest=e[1]

        graph.insert_edge(src,dest)

    return graph

