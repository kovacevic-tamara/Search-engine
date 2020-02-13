class Graph(object):
    recnik={}
    def __init__(self,recnik=None): #ako nema recnika ili je none ostavi
        if recnik== None:
            recnik={}
        self.recnik=recnik

    def vertices(self):
        return list(self.recnik.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self,vertex):
        if vertex not in self.recnik:
            self.recnik[vertex]=[]

    def add_edge(self,edge): #nalazi se izmedju 2 cvora
        edge=set(edge)
        (vertex1,vertex2)=tuple(edge) #tuple-isto sto i lista samo ne mozes menjati   tuple(python) = p y t h o n
        if vertex1 in self.recnik:
            self.recnik[vertex1].append(vertex2)
        else:
            self.recnik[vertex1]=[vertex2]

    def __generate_edges(self): #staticka
        edges=[]
        for vertex in self.recnik:
            for neighbour in self.recnik[vertex]:
                if {neighbour,vertex} not in edges:
                         edges.append({vertex,neighbour})
        return edges