// C++ program for implementation of Bubble sort 
#include <bits/stdc++.h> 
using namespace std; 

void swap(int *xPointer, int *yPointer)   // we are swaping by reference as to change the main array for the same.
{ 
   // its just swapping part 
	int temp = *xPointer; // here storing the xPointer in temp.
	*xPointer = *yPointer; 
	*yPointer = temp; 
} 

// A function to implement bubble sort 
void bubbleSort(int arr[], int n) 
{ 
	int i, j; 
	for (i = 0; i < n-1; i++)	 // here we have used n-1 as we would be comparing the j+1 with j in sub iteration part so to aviod address overflow.
	
	// Last i elements are already in place 
	for (j = 0; j < n-i-1; j++) 
		if (arr[j] > arr[j+1]) 
			swap(&arr[j], &arr[j+1]); 
} 

/* Function to print an array */
void printSortedArray(int arr[], int size) 
{ 
	int i; 
	for (i = 0; i < size; i++) 
		cout << arr[i] << " "; 
	cout << endl; 
} 

// Driver code 
int main() 
{ 
	int arr[] = {2,5,6,5,34,11,23,0,3}; 
	int n = sizeof(arr)/sizeof(arr[0]); 
	bubbleSort(arr, n); 
	cout<<"Bubble Sorted array: \n"; 
	printSortedArray(arr, n); 
	return 0; 
} 


