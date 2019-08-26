from collections import defaultdict
class Graph():
    def __init__(self,V):
        self.V = V
        self.graph = list()

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[yroot] = xroot
        elif rank[xroot] > rank[yroot]:
            parent[xroot] = yroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    def krusk(self):
        self.graph = sorted(self.graph, key = lambda x:x[2])
        res, rank, parent, i, e  = [], [], [], 0, 0
        for node in range(self.V):
            parent.append(node)
            rank.append(0)   
        while e < self.V-1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            print(x,y)
            if x != y:
                e += 1
                res.append([u, v, w])
                self.union(parent, rank, x, y)
                print('par:',parent)
                print('rank:',rank)
        for x in res:
            print(x)
g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
g.krusk()        

    
