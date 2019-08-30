for _ in range(int(input())):
    V = int(input())
    mat = []
    INF  = 9999999
    for i in range(V):
        t = list(map(int,input().split()))
        mat.append(t)
    d = mat

    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k]+ d[k][j]) 
                
    for i in d:
        print(*i)
                
