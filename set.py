#init add getitem remove clear, iteration za length
#java and python
class Set:
    def __init__(self,*args):
        self._dict={}
        for arg in args:
            if isinstance(arg,list):
                for i in arg:
                    self.add(i)
            else:
                self.add(arg)

    def add(self,item):
        if isinstance(item,list):
            for i in item:
                self._dict[i]=i
        else:
            self._dict[item]=item

    def remove(self,item):
        del self._dict[item]

    def contains(self,item):
        return item in self._dict

    __contains__=contains

    def __iter__(self):
        return iter(self._dict.copy())

    def __len__(self):
        return len(self._dict)

    def __copy__(self):
        return Set(self)

    def extend(self,args):
        for arg in args:
            self.add(arg)

def operation_and(listaRec1, listaRec2):
    resultSet = {}
    if listaRec1== False or listaRec2 == False:
        print("Nema zajednickog rezultata pretrage.")
    for html1 in listaRec1:
         for html2 in listaRec2:
              if html1 == html2:
                     resultSet[html1]=listaRec1[html1]+listaRec2[html1]
    return  resultSet

def operation_or(listaRec1,listaRec2):

    if listaRec1 == False and listaRec2 == False:
        print("Nema rezultata pretrage")
    elif listaRec1 == False:
        resultSet = listaRec2
    elif listaRec2 == False:
        resultSet=listaRec1
    else:
        resultSet = listaRec1
        for html in listaRec2:
            if html not in resultSet:
                resultSet[html]=listaRec2[html]
            else:
                resultSet[html]=listaRec1[html]+listaRec2[html]
    return print(resultSet)

        #python not java, znaci daj sve gde je pajton a nije java
def operation_not(listaRec1,listaRec2):
    resultSet = listaRec1
    for html in listaRec2:
         if html in resultSet:
                del resultSet[html]
    return resultSet

#def operation_and(set1,set2):
 #   for i in set1:
  #      if i not in set2:
   #         set2.remove(i)
    #return set2

#def operation_or(set1,set2):
 #   set1.extend(set2)
  #  return set1

#def operation_not(set1,set2):
 #   for i in set1:
  #      if i in set2:
   #         set2.remove(i)
    #return set2

