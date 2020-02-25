def my_parser(new_input):
    myRes=list()
    lparen = 0
    rparen = 0

    splitResult=new_input.split()
    n = len(splitResult)

    #ukucao je (dictionary || list || set) && ! tree
    # ['(dictionary', '||', 'list', '||', 'set)', '&&', '!', 'tree']
    #mora sve da se parsira, problem je (dictionart

    for i in range(n):
        if "(" in splitResult[i] and ")" in splitResult[i] and len(splitResult[i])>2:  #(bla)
            myRes.append("(")
            myRes.append(splitResult[i][1:len(splitResult[i])-1])
            myRes.append(")")
        elif "(" in splitResult[i] and  len(splitResult[i])>1: #(dictionary
            myRes.append("(")
            myRes.append(splitResult[i][1:len(splitResult[i])])
            lparen+=1
        elif ")" in splitResult[i] and len(splitResult[i])>1: #set)
            myRes.append(splitResult[i][0:len(splitResult[i])-1])
            myRes.append(")")
            rparen+=1
        elif "!" in splitResult[i] and len(splitResult[i])>1: #!tree
            myRes.append("!")
            myRes.append(splitResult[i][1:len(splitResult[i])])
        else:
            myRes.append(splitResult[i]) #|| list || && ! tree

            #myRes ['(', 'dictionary', '||', 'list', '||', 'set', ')', '&&', '!', 'tree'] sve je splitovano

    if rparen!=lparen:  #ili ce uci u prvi if pa ce biti nule ili ce ih pojedinacno prepoznati
        print("Pogrešan unos upita!")
        return

    #['(', 'dictionary', '||', 'list', '||', 'set', ')', '&&', '!', 'tree']
    for i in range(len(myRes)):  #proveri sve izuzetke
        if myRes[i]=="(": #kao je uneto ()
            try:
                if myRes[i+1]==")":
                    print("Nepravilan unos upita!")
                    return
            except IndexError:
                return -1
        if myRes[i] in ["&&","||"]:
            if i-1<0 or i+1>=len(myRes):   #ako je uneo && ili ||
                print("Nepravilan unos upita!")
                return
            if myRes[i-1] in ["(", "&&", "!","||"] or myRes[i+1] in [")", "&&","||"]:  #ako je uneto npr "(&&" ili "&&)"
                print("Nepravilan unos upita!")
                return
        elif myRes[i] not in ["(", "&&", "!","||", ")"]:
            try:
                if myRes[i+1] not in  ["(", "&&", "!","||", ")"]: #dictionary list==dictionari || list
                    myRes.insert(i+1,"||")
            except IndexError:
                continue
        elif myRes[i]=="!": #ako je uneto !&& !! !|| !)
            try:
                if myRes[i+1] in ["&&","!","||",")"]:
                    print("Nepravilan unos upita!")
                    return
            except IndexError:
                return -1

    return myRes