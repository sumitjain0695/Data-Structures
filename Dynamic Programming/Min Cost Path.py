def mincostpath(cost,m,n):
    R,C=map(int,input().split())
    l=[[0 for x in range(C)] for x in range(R)]
    print(l)
    l[0][0]=cost[0][0]
    print(l)
    for i in range(1,m+1):
        print('1st loop')
        l[i][0]=l[i-1][0]+cost[i][0]
        print(l)
    for j in range(1,n+1):
        print('2nd loop')
        l[0][j]=l[0][j-1]+cost[0][j]
        print(l)
    for i in range(1,m+1):
        for j in range(1,n+1):
            l[i][j]=min(l[i-1][j-1],l[i-1][j],l[i][j-1])+cost[i][j]
    print('final l',l)        
    return print(l[m][n])
costmat=[[1,2,3,5],[4,5,6,9],[8,6,4,3]]
mincostpath(costmat,2,3)
