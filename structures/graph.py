class Graph:
    def __init__(self):
        self._incoming={}
        self._outgoing={}

    def  insert_vertex(self,e):
        self._outgoing[e]=[]
        self._incoming[e]=[]

    def insert_edge(self,u,v):
        self._outgoing[u].append(v)
        self._incoming[v].append(u)

    def incoming_edges(self,v):
        inc= self._incoming
        return inc[v]

    def __str__(self):
        string=""

        for key in self._outgoing.keys():
            dic1=self._outgoing[key]
            dic2=self._incoming[key]

            for d in dic1.keys():
                string+= str("{}---->{}\n".format(" "*15,d))

            for d in dic2.keys():
                string+= str("{}<----{}\n".format(" "*15,d))

        return str(string)