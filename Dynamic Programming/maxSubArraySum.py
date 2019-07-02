for _ in range(int(input())):
    a=[int(x) for x in input().split()]
    m1 = -19999
    m2=0
    for i in range(0,len(a)): 
        m2 += a[i]
        if m1 < m2: 
            m1 = m2 
        if m2 < 0: 
            m2 = 0
    print(m1)
  
