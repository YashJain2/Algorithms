#include <iostream>
using namespace std;

//intializing globally
int r=3,c=3;
int arr[3][3]={ {2,45,0},
                {1,3,9},
                {78,67,10}
            };


void peak_2d(int row,int col){
  int mid=col/2,max=0,max_row;
  for(int i=0;i<row;i++){
    if(max<arr[i][mid]){
      max=arr[i][mid];
      max_row=i;
    }
  }
  if(max<arr[max_row][mid-1]){
    peak_2d(row,mid-1);
  }
  else if(max<arr[max_row][mid+1]){
    peak_2d(row,(col+mid));
  }
  else
    cout<<"Peak : "<<max;
}
//driver code
int main(){
  peak_2d(r,c);
  return 0;
}
