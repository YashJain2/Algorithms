#include <iostream>
using namespace std;
//MERGE SORT ALGORITHM
//step1-divide input array-2 parts, about midpoint so array of size n--n/2,n/2
//step2--sort the individual arrays
//step 3--merge by using 2 pointer approach
void merge(int *a,int s,int e)
{
    int mid=(s+e)/2;
    int i=s;
    int j=mid+1;
    int k=s;
    int temp[100];//temporary array to store result after merging
    while(i<=mid and j<=e)
    {
        if(a[i]<=a[j])
        {
            temp[k++]=a[i++]; //note-here instead of incrementing i,j,k after if else we can increment in the condition itself
        }
        else
        {
            temp[k++]=a[j++];
        }
    }
    while(i<=mid)
    {
        temp[k++]=a[i++];
    }
    while(j<=e)
    {
        temp[k++]=a[j++];
    }
    for(int i=s;i<=e;i++)
    {
        a[i]=temp[i];
    }
}
void mergesort(int a[],int s,int e)
{
    //base case
    if(s>=e)
    {
      return;
    }
    //step--1--divide
    int mid=(s+e)/2;
    //step--2--recursive sorting of divided array
    mergesort(a,s,mid);
    mergesort(a,mid+1,e);
    //step--3--merge the two arrays using 2 pointer approach

    merge(a,s,e);

}

int main() {
    int a[100];
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    mergesort(a,0,n-1);
        for(int i=0;i<n;i++)
{
    cout<<a[i]<<" ";
}
    return 0;
}
