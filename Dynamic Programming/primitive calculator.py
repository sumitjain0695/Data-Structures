def dp_sequence(n):
    sequence = []
    a = [0]*(n+1)
    for i in range(1,n+1):
        a[i] = a[i-1] + 1
        if (i%2 == 0):
            a[i] = min(1+a[i//2], a[i])
        if (i%3 == 0):
            a[i] = min(1+a[i//3], a[i])
    while (n>1):
        sequence.append(n)
        if (a[n-1] == a[n]-1):
            n = n-1
        elif (n%2 == 0 and (a[n//2] == a[n]-1)):
            n = n//2		
        elif (n%3 == 0 and (a[n//3] == a[n]-1)):
            n = n//3
    sequence.append(1)
    return list(reversed(sequence)),a

n = int(input())
sequence = (dp_sequence(n))
print(sequence)
print(len(sequence[0])-1)

