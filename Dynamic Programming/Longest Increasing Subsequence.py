def longinc():
    seq=[int(x) for x in input().split()]
    n=len(seq)
    temp=[1 for x in range(n)]
    for i in range(1,n):
        for j in range(0,i):
            if seq[i]>seq[j] and temp[i]<temp[j]+1:
                temp[i]=temp[j]+1
                
    return temp
print(longinc())
                


