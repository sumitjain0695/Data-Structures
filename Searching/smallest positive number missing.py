for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    l = [x for x in l if x>0]
    curr_min = 1
    st = 0
    end = len(l)
    maximum = max(l)
    ind_l = [0 for x in range(maximum)]
    #print(ind_l)
    for i in l:
        ind_l[i-1] = 1
    #print(ind_l)
    try:
        print(ind_l.index(0)+1)
    except:
        print(maximum+1)
        
