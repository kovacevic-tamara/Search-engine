def convert_in_pos(myRes):
    #funkcija koja prebacuje iz infiksne u postfiksnu notaciju
    #myRes=['(', 'dictionary', '||', 'list', '||', 'set', ')', '&&', '!', 'tree']
    # rezultat treba da bude dictionary list set || || tree! &&']
    stek=list()
    resultList=list()

    myOperators={"!":3, "&&":2,"||":1}
    for i in myRes:
        if i == "(":    #dodaj je na stek
            stek.append(i)
        if i==")":  #na steku ce se nalaziti operacije i zagrade, kada dodje do zatvorene zagrade sve operacije sa steka, do ovorene zagrade pushovace na result set
            while stek[len(stek)-1]!="(":
                vrednost=stek.pop()
                resultList.append(vrednost)
            stek.pop()
        if i in myOperators.keys():
            while len(stek) > 0 and stek[len(stek) - 1] != "(" and myOperators[stek[len(stek) - 1]] > myOperators[i]:
                vrednost=stek.pop()
                resultList.append(vrednost)
            stek.append(i)
        if i not in ["!", "&&", "||", "(",")"]:
            resultList.append(i)

    while len(stek)>0:
        vrednost=stek.pop()
        resultList.append(vrednost)

    return resultList