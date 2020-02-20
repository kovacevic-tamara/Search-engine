def heap_sort(resultSet): #stize mi html stranica kao kljuc i rank kao vrednost
    list=[]
    sorted_result={}
    for val in resultSet.values():
        list.append(val)
    list=list.copy()
    build_heap(list)
    sorted_list=[]
    for _ in range(len(list)):
        list[0],list[-1]=list[-1],list[0]
        sorted_list.append(list.pop())
        min_heapify(list,0)

    sorted_list2=[]
    for i in reversed(sorted_list):
        sorted_list2.append(i)

    for res in sorted_list2:
        for key,values in resultSet.items():
            if res==values:
                sorted_result[key]=values
    return  sorted_result


def build_heap(list):
    for i in reversed(range(len(list)//2)):
        min_heapify(list,i)

def min_heapify(list,i):
    left=2*i+1
    right=2*i+2
    length=len(list)-1
    mini=i
    if left<=length and list[i]>list[left]:
        mini=left
    if right<=length and list[mini]>list[right]:
        mini=right
    if mini!=i:
        list[i],list[mini]=list[mini], list[i]
        min_heapify(list,mini)