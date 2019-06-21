n=int(input())
l = []
for i in range(n):
    m=int(input())
    l.append(m)   
st = 0
en = n - 1
while st < en :
    mid = (st + en)//2
    if l[mid] > l[mid + 1] :
        ans = mid
        break
    elif l[mid] < l[mid - 1] :
        ans = mid - 1
        break
    elif l[mid] > l[0] :
        st = mid
    elif l[mid] < l[0] :
        en = mid
print(ans)        
        
            
