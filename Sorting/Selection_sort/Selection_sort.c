#include<stdio.h>
#include<stdlib.h>
int i;
void SelectionSort(int a[], int n)
{
    int j;
    for(i=0;i<n-1;i++)
    {
        int min = i;
        for(j = i+1;j < n;j++)
        {
            if(a[j] < a[min])
               {

                   min = j;
               }
        }
        if(min != i)
        {
            int temp = a[i];
            a[i] = a[min];
            a[min] = temp;
        }
    }
    printf("The array is sorted !!!\n");
    for(i = 0; i < n; i++)
    {
        printf("%d\t",a[i]);
    }
}

int main()
{
    int n;
    printf("Enter size of array : ");
    scanf("%d",&n);
    int a[n];
    printf("Enter elements of array : \n");
    for(i = 0;i < n;i++)
    {
        printf("Enter element %d : ",i+1);
        scanf("%d",&a[i]);
    }
    SelectionSort(a,n);
    return 0;
}

//Input :
//Size of array : 9
//Elements : 2,5,6,5,34,11,23,0,3
//Output :
//The array is sorted
// 0    2   3   5   5   6   11  23  34
