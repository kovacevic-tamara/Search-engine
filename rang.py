#fixme netacan unos

def rang(resultSet,graph):
    brojac = 0  # broj trazenih reci u stranicaama koje ukazuju na moju

    for res in resultSet.keys():
        rank={}
        br=resultSet[res]
        incom=graph.incoming_edges(res) #lista izlaznih grana iz mog cvora
        br_inc_reci=0
        br_inc=0


        for i in incom:
            if i in resultSet.keys():
                print("MOOOOOOOOOOOOOOOOOOOOOOLIM TEEEEEE")
                br_inc_reci+=(resultSet[i])
                br_inc+=3 ##########################################fixme
            else:
                br_inc+=1
        rank[res]=br+round(0.8*br_inc)+round(0.6*br_inc_reci)
    print(rank)
    return rank

def heap_sort(resultSet): #stize mi html stranica kao kljuc i rank kao vrednost
    list=[]
    sorted_result={}
    for val in resultSet.values():
        list.append(val)
    list=list.copy()
    build_heap(list)
    sorted_list=[]
    for _ in range(len(list)):
        list[0],list[-1]=list[-1],list[0]
        sorted_list.append(list.pop())
        min_heapify(list,0)

    sorted_list2=[]
    for i in reversed(sorted_list):
        sorted_list2.append(i)

    for res in sorted_list2:
        for key,values in resultSet.items():
            if res==values:
                sorted_result[key]=values
    return  sorted_result


def build_heap(list):
    for i in reversed(range(len(list)//2)):
        min_heapify(list,i)

def min_heapify(list,i):
    left=2*i+1
    right=2*i+2
    length=len(list)-1
    mini=i
    if left<=length and list[i]>list[left]:
        mini=left
    if right<=length and list[mini]>list[right]:
        mini=right
    if mini!=i:
        list[i],list[mini]=list[mini], list[i]
        min_heapify(list,mini)

def prikaz(resultSet):
    running=1
    ponovo=True
    while running:
        if ponovo==True: #kad pukne da sve vrati na pocetak
            j=0
            ispisano=0
            flag=False
            ponovo=False

        print("\nOpcije:\n (*)izbor broja stranica \n (+)prikaz sledecih n stranica\n (-)prikaz prethodnih n stranica\n (q)izlaz")
        try:
            unos = str(input(">> "))
        except ValueError:
            print("Izaberite opciju iz  menija!\n")
            continue


        if unos == "q":
            return
        elif unos == "+":
            if n==0:
                print("Neophodno je da uneste broj stranica za prikaz!")
                continue
            flag = False
        elif unos == "-":
            if n==0:
                print("Neophodno je da uneste broj stranica za prikaz!")
                continue
            flag = True
        elif unos == "*":
            try:
                print("Unesite zeljeni broj stranica za prikaz (ukupno:{})".format(len(resultSet)))
                n = int(input("-> "))
            except ValueError:
                print("Molimo ponovite izbor ->* Unositi iskljucivo celobrojne vrednosti!")
                continue
            i = 0
            ispisano = 0
            flag = False
        else:
            ponovo=True
            print("Molimo ponovite izbor.Izaberite opciju iz ponuđenog menija!")
            continue

        brojac=-1 #sluzi da indeksira result Set da krene bas od tog odakle treba, jedan nakon ispisanog
        if flag == False:
            j=0
            if len(resultSet) - ispisano >= n:  # pokriva slucaj kada imam 6 n=4
                for set in resultSet:
                    brojac=brojac+1
                    if brojac==ispisano:
                        if j<n:
                            print("{}               {}".format(set, resultSet[set]))
                            ispisano=ispisano+1
                            j =j+ 1
            else:
                if len(resultSet)==ispisano:
                    print("Dosli ste do kraja spiska!")
                else:
                    print("Nije moguc prikaz!")

        else:#za minus
            j=0
            if ispisano-2*n>=0:
                ispisano=ispisano-n*2
                for set in resultSet:
                    brojac = brojac + 1
                    #u ispisano imam dokle je stigao
                    if brojac == ispisano:
                        if j < n:
                            print("{}               {}".format(set, resultSet[set]))
                            ispisano = ispisano + 1
                            j = j + 1
            else:
                print("Dosli ste na pocetak spiska!")
