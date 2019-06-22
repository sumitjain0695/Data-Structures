for _ in range(int(input())):
    n, s = map(int,input().split())
    l = sorted([int(x) for x in input().split()])
    i=0
    j=1
    f=0
    while i < n and j < n:
        #print('looping')
        if i != j and l[j] - l[i] == s :
            #print('found',l[i],l[j])
            f=1
            break
        elif l[j] - l[i] < s :
            j+=1
        else:
            i+=1
    if f == 0:
        print('-1')
    else:
        print('1')
            
    
        
