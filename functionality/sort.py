def heap_sort(resultSet): #stize mi html stranica kao kljuc i rank kao vrednost
    list=[]
    result={}
    for val in resultSet.values():
        list.append(val)

    build_heap(list)
    sorted_list=[]

    for a in range(len(list)):
        list[0],list[-1]=list[-1],list[0]
        sorted_list.append(list.pop())
        heap_max(list,0)

    for res in sorted_list:
        for key,values in resultSet.items():
            if res==values:
                result[key]=values

    return result

def build_heap(list):
    for i in reversed(range(len(list)//2)):
        heap_max(list,i)

def heap_max(list,i):
    left=2*i+1
    right=2*i+2
    length=len(list)-1
    max_el=i
    if left<=length and list[i]<list[left]:
        max_el=left
    if right<=length and list[max_el]<list[right]:
        max_el=right
    if max_el!=i:
        list[i],list[max_el]=list[max_el], list[i]
        heap_max(list,max_el)