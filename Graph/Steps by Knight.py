def isInside(x, y, N): 
    if (x >= 1 and x <= N and y >= 1 and y <= N):  
        return True
    return False
    
for _ in range(int(input())):
    n = int(input())
    kx, ky = map(int,input().split())
    tx, ty = map(int,input().split())
    combx = [2, 2, -2, -2, 1, 1, -1, -1] 
    comby = [1, -1, 1, -1, 2, -2, 2, -2]
    q = []
    q.append([kx,ky,0])
    visited = [[False for x in range(n+1)] for x in range(n+1)]
    visited[kx][ky] = True
    while len(q) > 0:
        temp = q.pop(0)
        if temp[0] == tx and temp[1] ==ty:
            print(temp[2])
        for i in range(8):
            x = temp[0] + combx[i]
            y = temp[1] + comby[i]
            if isInside(x, y, n) and not visited[x][y]:
                visited[x][y] = True
                q.append([x, y, temp[2] + 1])
                
            
