class Graph():
    def __init__(self, V): 
        self.V = V
        self.graph = [[0 for column in range(V)] for row in range(V)] 

    def minKey(self, key, mstSet):
        mini = float('inf')
        for i in range(self.V): 
            if key[i] < mini and mstSet[i] == False: 
                mini = key[i] 
                min_index = i
        return min_index
    
    def prim(self):
        key = [1000000009] * self.V
        key[0] = 0
        parent = [0] * self.V
        parent[0] = -1
        mstSet = [False] * self.V
        for i in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for j in range(self.V):
                if self.graph[u][j] != 0 and mstSet[j] == False and key[j] >self.graph[u][j]:
                    key[j] = self.graph[u][j]
                    parent[j] = u
        return parent        
g = Graph(5) 
g.graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
  
print(g.prim())     

    
