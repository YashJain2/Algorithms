#include <iostream>
using namespace std;
int partition(int a[],long long int s,long long int e)
{
long long int i=s-1;
long long int j=s;
long long int pivot=a[e];
for(j=s;j<=e-1;j++)
{
    if(a[j]<=pivot)
    {
        i=i+1;
        swap(a[i],a[j]);
    }
}
swap(a[i+1],a[e]);
return i+1;
}
void quick_sort(int a[],long long int s,long long int e){
    if(s>=e)
    {
        return;
    }
    //rec case
    long long int p=partition(a,s,e);
    quick_sort(a,s,p-1);
    quick_sort(a,p+1,e);
}

int main() {
    //quicksort algorithm
    //divide and conquer strategy
    //nlogn time for average case
    //n^2 for worst case,inplace sort algorithm, wont take extra space
	long long int n;
   
	cin>>n;
	 int arr[n];
    for(int i=0;i<n;i++)
	{
		cin>>arr[i];
	}
    quick_sort(arr,0,n-1);
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;

}

//OUTPUT:
//1 2 3 4 6