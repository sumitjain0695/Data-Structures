#include<iostream>
using namespace std;
int main()
{
    int n,m;
    cin>>n;
    int d[n];
    for(int i=0;i<n;i++)
        cin>>d[i];
    cin>>m;
    int b[m];
    for(int i=0;i<m;i++)
        cin>>b[i];
    int f[n]={0},a[m]={0};
    for(int i=0;i<m;i++)
    {
        for(int j=n-1;j>=0;j--)
        {
            if(f[j]<j+1)
            {
                if(d[j]>=b[i])
                {
                    f[j]++;
                    a[i]=j+1;
                    break;
                }
            }
        }
    }
    for(int i=0;i<m;i++)
    {
        cout<<a[i];
        if(i<m-1)
            cout<<" ";
    }
}
