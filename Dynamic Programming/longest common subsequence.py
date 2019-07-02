def lcs():
    X=input('1st string ')
    Y=input('2nd string ')
    l=[[0 for x in range(len(Y)+1)] for x in range(len(X)+1)]
    for i in range(len(X)+1):
        for j in range(len(Y)+1):
            if i==0 or j==0:
                l[i][j]=0
            elif X[i-1]==Y[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    last=l[len(X)][len(Y)]
    i=len(X)
    j=len(Y)
    seq=[]
    while i>0 and j>0:
        if X[i-1]==Y[j-1]:
            seq.append(X[i-1])
            j-=1
            i-=1
        elif l[i-1][j]>l[i][j-1]:
            i-=1
        else:
            j-=1
    return ''.join(seq[::-1])       

L=lcs()    
print(L)
    
    
