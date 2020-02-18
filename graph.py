class Vertex:
    def __init__(self,page):
        self._html_page=page

    def html_page(self):
        return self._html_page

    def __str__(self):
        return str(self._html_page)

    def __hash__(self):
        return hash(id(self))

class Edge:
    def __init__(self,u,v):
        self.origin=u
        self.destination=v

    def __hash__(self):
        return hash((self.origin,self.destination))

    def __str__(self):
        return str(self.origin)+ "------->"+ str(self.destination)

class Graph:
    def __init__(self):
        self._incoming={}
        self._outgoing={}

    def vertices(self):
        return list(self._outgoing.keys())

    def  insert_vertex(self,e):
        v=Vertex(e)
        self._outgoing[v]={}
        self._incoming[v]={}
        return v

    def insert_edge(self,u,v):
        e=Edge(u,v)
        self. _outgoing[u][v]=e
        self._incoming[v][u]=e

    def incoming_edges(self,v):
        inc= self._incoming  #adj u keys ima granu a u values njene incomingre
        result=list()
        for key in inc.keys():
            if str(key)==str(v):
                for edge in inc[key].values():
                   # print(edge)
                    yield edge
             #omogucava "vise povratnih vrednosti"

    def __str__(self):
        string=""

        for key in self._outgoing.keys():
            dic1=self._outgoing[key]
            dic2=self._incoming[key]

            for d in dic1.keys():
                string+= str("{}------>{}\n".format(" "*20,d))

            for d in dic2.keys():
                string+= str("{}<------{}\n".format(" "*20,d))

        return str(string)