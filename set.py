    #java and python
def operation_and(listaRec1, listaRec2):
    resultSet = {}
    for html1 in listaRec1.keys():
        for html2 in listaRec2.keys():
            if html1 == html2.keys():
                resultSet[html1]=listaRec1[html1]+listaRec2[html1]

    return  resultSet

def operation_or(listaRec1,listaRec2):
    resultSet=listaRec1
    for html in listaRec2.keys():
        if html not in resultSet.keys():
            resultSet[html]=listaRec2[html]
        else:
            resultSet[html]=listaRec1[html]+listaRec2[html]
    return resultSet

#python not java, znaci daj sve gde je pajton a nije java
def operation_not(listaRec1,listaRec2):
    resultSet = listaRec1
    for html in listaRec2.keys():
        if html in resultSet.keys():
            del resultSet[html]

    return resultSet
