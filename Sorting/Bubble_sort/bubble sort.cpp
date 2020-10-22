#include<iostream>

using namespace std;

int main()
{
	int a[50],num,i,j,temp;
	cout<<"Enter the size of array: ";
	cin>>num;
	cout<<"Enter the array elements: ";

	for(i=0;i<num;++i)
		cin>>a[i];

	for(i=1;i<num;++i)
	{
		for(j=0;j<(num-i);++j)
			if(a[j]>a[j+1])
			{
				temp=a[j];
				a[j]=a[j+1];
				a[j+1]=temp;
			}
	}

	cout<<"Array after bubble sort:";
	for(i=0;i<num;++i)
		cout<<" "<<a[i];

	return 0;
}
