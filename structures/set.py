class Set():
    def __init__(self):
        self.resultSet={}

    def operation_and(self,recnik1, recnik2):
        self.resultSet={}
        if recnik1== False or recnik2 == False:
            print("Nema zajedničkog rezultata pretrage.")
            return self.resultSet
        for html1 in recnik1:
             for html2 in recnik2:
                  if html1 == html2:
                         self.resultSet[html1]=recnik1[html1]+recnik2[html1]
        return  self.resultSet

    def operation_or(self,recnik1,recnik2):
        self.resultSet = {}
        if recnik1 == False and recnik2 == False:
            print("Nema rezultata pretrage.")
        elif recnik1 == False:
            self.resultSet = recnik2
        elif recnik2 == False:
            self.resultSet=recnik1
        else:
            self.resultSet = recnik1
            for html in recnik2:
                if html not in self.resultSet:
                    self.resultSet[html]=recnik2[html]
                else:
                    self.resultSet[html]=recnik1[html]+recnik2[html]
        return self.resultSet

    def operation_not(self,recnik1,recnik2):
        self.resultSet = recnik1
        for html in recnik2:
             if html in self.resultSet:
                    del self.resultSet[html]
        return self.resultSet