from collections import defaultdict
class Graph():
    def __init__(self,V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, u, color):
        color[u] = 'gray'
        for v in self.graph[u]:
            if color[v] == 'gray':
                return True
            if color[v] == 'white' and self.dfs(v, color) == True:
                return True
        color[u] = 'black'
        return False
    def checkCycle(self):
        color = ['white']*self.V
        for i in range(self.V):
            if color[i] == 'white':
                if self.dfs(i, color) == True:
                    return True
        return False
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)
print(g.checkCycle())
            
            
