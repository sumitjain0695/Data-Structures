class Graph():
    def __init__(self, V): 
        self.V = V 
        self.graph = [[0 for column in range(V)] for row in range(V)]
    def isBipartite(self):
        start = 0
        for i in range(len(list(self.graph))):
            if 1 in self.graph[i]:
                start = i
                break
        col = [-1] * self.V 
        col[start] = 1
        q = [] 
        q.append(start) 
        while q: 
            u = q.pop() 
            if self.graph[u][u] == 1: 
                return False
            for v in range(self.V): 
                if self.graph[u][v] == 1 and col[v] == -1: 
                    col[v] = 1 - col[u] 
                    q.append(v) 
                elif self.graph[u][v] == 1 and col[v] == col[u]: 
                    return False
        return True    
g = Graph(4) 
g.graph = [[0, 1, 0, 1],[1, 0, 1, 0],[0, 1, 0, 1],[1, 0, 1, 0]] 
              
print(g.isBipartite())
  
