class ComplexTree(object):
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

#['dictionary', 'list', 'set', '||', '||', 'tree', '!', '&&']
#set=[dictionary,list,set]
#|| ->  list || set
#|| -> dictionari || list || set
#tree
#!tree
#(dictionary || list || set) && !tree

def create_tree(resultList,trie):
    stek=list()

    for i in resultList:
        if i=="!":                    #ako naidjes na ! skini poslednji i vrati
            operation=ComplexTree(i)
            operand=stek.pop()
            operation.left=operand

            stek.append(operation)
        elif i in ["&&", "||"]:        #ako dodjes do neke operacije,skini poslednje dve reci sa steka, vratio kao operaciju
            operation=ComplexTree(i)
            operand_right=stek.pop()
            operand_left=stek.pop()

            operation.left=operand_left
            operation.right=operand_right

            stek.append(operation)
        else:                           #ako naidje na rec nadji je i salji rezultat pretrage na stek
            result=trie.pretraga(i)
            #print(result)
            if result:
                operand=ComplexTree(result)
            else:
                operand=ComplexTree({})
            stek.append(operand)