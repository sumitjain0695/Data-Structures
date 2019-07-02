def edit():
    str1=input('enter string 1')
    str2=input('enter string 2')
    dp=[[0 for x in range(len(str2)+1)] for x in range(len(str1)+1)]
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
    return(dp)
l=edit()
print(l,end='\n')
