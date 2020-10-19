#include<bits/stdc++.h>
# define mp make_pair
# define pb push_back
# define pp pair<int,int>
#define fast ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define ll long long
#define M 1000000007
using namespace std;
int ChainMatrix(int p[], int n) 
{ 
	int dp[n][n];
	for (int i=0; i<n; i++) 
        dp[i][i] = 0; 
    for (int j=1; j<n-1; j++)
    {  
	    for (int i=1; i<n-j; i++)      
	        dp[i][i+j] = min(dp[i+1][i+j] + p[i-1]*p[i]*p[i+j],dp[i][i+j-1] + p[i-1]*p[i+j-1]*p[i+j]);      
    }
    return dp[1][n-1];
} 

int main()
{
	fast
	int A[3] = {5,10,15}; 
    cout <<"Min multiplications are "<<ChainMatrix(A,3);
	return 0;

} 
