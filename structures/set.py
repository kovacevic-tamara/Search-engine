class Set():
    def operation_and(self,recnik1, recnik2):
        resultSet = {}
        if recnik1== False or recnik2 == False:
            print("Nema zajednickog rezultata pretrage.")
            return resultSet
        for html1 in recnik1:
             for html2 in recnik2:
                  if html1 == html2:
                         resultSet[html1]=recnik1[html1]+recnik2[html1]
        return  resultSet

    def operation_or(self,recnik1,recnik2):
        resultSet = {}

        if recnik1 == False and recnik2 == False:
            print("Nema rezultata pretrage")
        elif recnik1 == False:
            resultSet = recnik2
        elif recnik2 == False:
            resultSet=recnik1
        else:
            resultSet = recnik1
            for html in recnik2:
                if html not in resultSet:
                    resultSet[html]=recnik2[html]
                else:
                    resultSet[html]=recnik1[html]+recnik2[html]
        return resultSet

    def operation_not(self,recnik1,recnik2):
        resultSet = recnik1
        for html in recnik2:
             if html in resultSet:
                    del resultSet[html]
        return resultSet