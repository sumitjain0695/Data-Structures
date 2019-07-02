from collections import Counter
def get_all_substrings(string):
    length = len(string)
    alist = []
    for i in range(length):
        if string[i]==string[0]:
            for j in range(i,length):
                if string[i:j + 1] not in alist:
                    alist.append((string[i:j + 1],string.count(string[i:j+1]))) 
    return alist

for _ in range(int(input())):
    n=int(input())
    string=input()
    strset=get_all_substrings(string)
    #print(strset)
    ctr=Counter(strset)
    maxval=max(ctr.values())
    maxcnt=[i for i,j in ctr.items() if j==maxval]
    print(max(maxcnt,key=len))    
            
    
        
        
        
       
            
            

        
    
        
    
    
        
    
        
    
    
