#prikaz stranica- prikazuje iskljucivo onoliko stranica koliko je n, ukoliko nije moguce prikazati tacan broj stranica,
#prikaz nece biti moguc
def prikaz(resultSet):
    running=1
    ponovo=True

    if len(resultSet) == 0:
        print("Nema rezultata pretrage.\n")
        return

    while running:
        if ponovo==True: #kad pukne da sve vrati na pocetak
            j=0
            ispisano=0
            flag=False
            ponovo=False
        print("\nUkupno je pronađeno {} rezultat/a pretrage.".format(len(resultSet)))
        print("\nOpcije ispisa dobijenih rezultata:\n (*)->izbor broja stranica \n (+)->prikaz sledecih n stranica\n (-)->prikaz prethodnih n stranica\n (q)->izlaz")
        try:
            unos = str(input(">> "))
        except ValueError:
            print("Izaberite opciju iz  menija!\n")
            continue

        if unos == "q":
            running=1
            break
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
                print("Unesite željeni broj stranica za prikaz")
                n = int(input("-> "))
                print("{:150s} {:4s}".format("PUTANJA DO HTML STRANICE", "RANG"))
                print('-' * 155)
            except ValueError:
                print("Molimo ponovite izbor -> * Unositi iskljucivo celobrojne vrednosti!")
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
                            print("{:150s} {:4d}".format(set, resultSet[set]))
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
                            print("{:150s} {:4f}".format(set, resultSet[set]))
                            ispisano = ispisano + 1
                            j = j + 1
            else:
                print("Dosli ste na pocetak spiska!")