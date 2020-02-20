def operation_and(listaRec1, listaRec2):
    resultSet = {}
    if listaRec1== False or listaRec2 == False:
        print("Nema zajednickog rezultata pretrage.")
        return resultSet
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