class Element(object):
    def __init__(self,slovo,roditelj):
        self.slovo = slovo
        self.roditelj = roditelj
        self.deca = []
        self.recnik = None

    def __eq__(self, drugo_slovo):
        return self.slovo == drugo_slovo

    def __str__(self):
        return self.slovo

class Trie():
    def __init__(self,koren):
        self.koren = koren

    def dodaj_rec(self,rec,putanja_fajla):
        lista_elemenata = []
        for i in range(len(rec)):
            element = Element(rec[i],None)
            if i == len(rec):
                element.recnik = {putanja_fajla:1}
            lista_elemenata.append(element)
        self.rasporedi_slova(lista_elemenata,self.koren,putanja_fajla)

    def dodaj(self,element,roditelj):
        element.roditelj = roditelj
        roditelj.deca.append(element)

    def rasporedi_slova(self, lista_elemenata, koren, putanja_fajla):
            trenutni_element = lista_elemenata[0]
            if trenutni_element not in koren.deca:
                for element in lista_elemenata:
                    self.dodaj(element, koren)
                    koren = element
                element.recnik = {putanja_fajla:1}
            else:
                for dete in koren.deca:
                    if trenutni_element == dete:
                        lista_elemenata = lista_elemenata[1:]
                        if len(lista_elemenata)>0:
                            self.rasporedi_slova(lista_elemenata,dete,putanja_fajla)
                        else:
                            if dete.recnik == None:
                                dete.recnik = {putanja_fajla:1}
                            elif putanja_fajla not in dete.recnik:
                                dete.recnik[putanja_fajla] = 0
                            dete.recnik[putanja_fajla] +=1

    def pretraga(self, rec):
        trenutni = self.koren
        for slovo in rec:
            if slovo not in trenutni.deca:
                return False
            else:
                element = trenutni.deca[trenutni.deca.index(slovo)]
            trenutni = element
        if trenutni.recnik != None:
            return trenutni.recnik
        else:
            return False

if __name__ == "__main__":
    trie = Trie(Element("KOREN",None))
    trie.dodaj_rec('anja','link1')
    trie.dodaj_rec('jovana','link2')
    trie.dodaj_rec('goga','link2')
    trie.dodaj_rec('anja','link3')
    trie.dodaj_rec('anja','link1')
    recnik = {'jovana':1,'annja':2,'milica':30}
    print(recnik)
    recnik2 = trie.pretraga('anja')
    print(recnik2)