class ResultSet:
    #java and python
    def operation_and(listaRec1, listaRec2):
        resultSet = list()
        for html1 in listaRec1:
            for html2 in listaRec2:
                if html1 == html2:
                    resultSet.append(html1)
            
        return  resultSet

    def operation_or(listaRec1,listaRec2):
        resultSet=list()
        for html1 in listaRec1:
            resultSet.append(html1)

        for html2 in listaRec2:
            if html2 not in resultSet: #ako je isti kao html1 i vec dodat ne treba opet
                resultSet.append(html2)

        return resultSet

#python not java, znaci daj sve gde je pajton a nije java
    def operation_not(listaRec1,listaRec2):
        resultSet = list()
        for html1 in listaRec1:
            brojac=0
            for html2 in listaRec2:
                if html1 == html2:      #ako ima i javu podigni brojac,ako nema javu brojac=0
                    brojac=brojac+1

            if brojac == 0:
                resultSet.append(html1)

        return resultSet