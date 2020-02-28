from complex_query.complex_trie import create_tree
from complex_query.infix_postfix import convert_in_pos
from complex_query.my_complex_parser import my_parser


def complex_function(graph,trie,new_input):
    myRes=my_parser(new_input)
    #print(myRes)

    if myRes==None:
        return -1
    resultList=convert_in_pos(myRes)

    #print(resultList)

    root=create_tree(resultList,trie)