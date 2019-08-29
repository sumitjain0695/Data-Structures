class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = []
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    def bellman(self, start):
        d = [float('inf')]*self.V
        d[start] = 0
        for i in range(self.V-1):
            for u, v, w in self.graph:
                if d[u] != float('inf') and d[v] > d[u] + w:
                    d[v] = d[u] + w

        for u, v, w in self.graph:
                if d[u] != float('inf') and d[v] > d[u] + w:
                    print('-ve cycle!!!!!!!!!!!')
                    return
        for i in range(self.V):
            print(i, d[i])
g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
g.bellman(0)            
            
