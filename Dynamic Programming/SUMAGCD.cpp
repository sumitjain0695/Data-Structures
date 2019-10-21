#include<iostream>
using namespace std;
int gcd0(unsigned int a,unsigned int b)
{
    if (a == 0)
        return b;
    return gcd0(b % a, a);
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        unsigned long int n,cnt=0;
        cin>>n;
        unsigned long int s[n],max1=0,min1,gcd;
        for(unsigned long int i=0;i<n;i++)
        {
            cin>>s[i];
            if(i==0||min1>s[i])
                min1=s[i];
            if(max1<s[i])
            {
                max1=s[i];
                cnt=0;
            }
            if(s[i]==max1)
                cnt++;
        }
        if(cnt==n)
            cout<<2*max1<<endl;
        else
        {
            gcd=min1;
            for(unsigned long int i=0;i<n;i++)
            {
                if(gcd==1)
                    break;
                else
                    if(s[i]!=max1&&s[i]!=min1)
                        gcd=gcd0(s[i],gcd);
            }
            cout<<gcd+max1<<endl;
        }
    }
}
