class Element(object):
    def __init__(self,slovo,roditelj):
        self.slovo = slovo
        self.roditelj = roditelj
        self.deca = []
        self.oznaka_kraja = False

    def __eq__(self, drugo_slovo):
        return self.slovo == drugo_slovo

    def __str__(self):
        return self.slovo

class Trie():
    def __init__(self,koren):
        self.koren = koren
        self.recnik = {}

    def dodaj_rec(self,rec,putanja_fajla):
        lista_elemenata = []

        for i in range(len(rec)):
            element = Element(rec[i],None)
            if i == len(rec):
                element.oznaka_kraja = True
            lista_elemenata.append(element)
        self.rasporedi_slova(rec,lista_elemenata,self.koren,putanja_fajla)

    def dodaj(self,element,roditelj):
        element.roditelj = roditelj
        roditelj.deca.append(element)

    def rasporedi_slova(self,rec, lista_elemenata, koren, putanja_fajla):
        trenutni_element = lista_elemenata[0]
        if trenutni_element not in koren.deca:
            for element in lista_elemenata:
                self.dodaj(element, koren)
                koren = element
            element.oznaka_kraja = True
            self.recnik[rec]={}
            self.recnik[rec][putanja_fajla] = 1
        else:
            for dete in koren.deca:
                if trenutni_element == dete:
                    lista_elemenata = lista_elemenata[1:]
                    if len(lista_elemenata)>0:
                        self.rasporedi_slova(rec,lista_elemenata,dete,putanja_fajla)
                    else:
                        if dete.oznaka_kraja == True:
                            self.recnik[rec][putanja_fajla] = 1

    def pretraga(self, rec):
        return self.recnik[rec]