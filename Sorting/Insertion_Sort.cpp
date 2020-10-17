#include<iostream>
using namespace std;

//Time complexity : O(n^2)
//comparision sorting
//not used for large data sorting
void insertionSort(int a[],int size)
{
  int i,j,key;
  for(i=1;i<=size-1;i++)
  {
    key=a[i];
    j=i;
    while (a[j-1]>key && j>=1)
    {
      a[j]=a[j-1];
      j--;
    }
    a[j]=key;
  }
  for (int k=0;k<size;k++)
    cout<<a[k]<<"\t";
}


int main()
{
  int a[]={34,2,42,1,11,23};
  int n=sizeof(a)/sizeof(a[0]);
  insertionSort(a,n);
  return 0;
}
