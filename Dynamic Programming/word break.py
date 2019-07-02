def wordbreak(s,dic):
    n=len(s)
    ans=[False for i in range(n+1)]
    ans[0]=True
    for i in range(n):
        if ans[i]==True:
            for word in dic:
                l=len(word)
                if i+l<=n and s[i:i+l]==word:
                    ans[i+l]=True
    return ans
print(wordbreak('ilikemango',["mobile","samsung","sam", 
                           "sung","ma","mango", 
                           "icecream","and","i", 
                           "like","ice","cream"]))

            
