def count(S, m, n): 
    table = [0 for k in range(n+1)] 
    table[0] = 1
    for i in range(0,m):
        print('i= ',i,'num= ',S[i])
        print(list(int(x) for x in range(13)))
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
            print('j=',j,table)
    return table
arr = [1, 3, 5] 
m = len(arr) 
n = 12
x = count(arr, m, n) 
print (x) 
