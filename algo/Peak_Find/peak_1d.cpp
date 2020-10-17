#include<iostream>
using namespace std;

//using divide and conquer approach
//time complexity:O(logn)
void peak_1d(int arr[],int size){
  int mid=size/2;
  if(arr[mid]<arr[mid-1]){
    peak_1d(arr,mid-1);
  }
  else if(arr[mid]<arr[mid+1]){
    peak_1d(arr,size+mid/2);
  }
  else
  cout<<"Peak : "<<arr[mid];
}

int main(){
  int arr[9]={2,5,6,5,34,11,23,0,3};
  peak_1d(arr,9);
  return 0;
}
