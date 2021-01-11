
graph_elements = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"]
}

class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # displaying graph vertices
    def get_vertices(self):
        return list(self.gdict.keys())
    
    # displaying graph edges
    def get_edges(self):
        edge_name = []
        for v in self.gdict:
            for nv in self.gdict[v]:
                if {nv, v} not in edge_name:
                    edge_name.append({v, nv})
        return edge_name

    def edges(self):
        return self.get_edges()

    # adding a vertex
    def add_vertex(self, v):
        if v not in self.gdict:
            self.gdict[v] = []
    
    # adding an edge
    def add_edge(self,edge):
        edge = set(edge)
        (v1, v2) = tuple(edge)
        if v1 in self.gdict:
            self.gdict[v1].append(v2)
        else:
            self.gdict[v1] = v2



g = graph(graph_elements)
print(g.get_vertices())
print(g.edges())
g.add_vertex('f')
print(g.get_vertices())

e1 ={'a', 'e'}
e2 = {'a', 'c'}

g.add_edge(e1)
g.add_edge(e2)
print(g.edges())



