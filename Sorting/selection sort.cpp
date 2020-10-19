// To sort the given array using Selection sort

#include<stdio.h>

int main()
{
    int i,j,num,k,temp,min,a[30];
    printf("Enter the number of elements:");
    scanf("%d",&num);
    printf("\nEnter the elementsto be sorted\n");

    for(i=0;i<num;i++)
    {
        scanf("%d",&a[i]);
    }

    for(i=0;i<num-1;i++)
    {
        min=a[i];
        k=i;
        for(j=i+1;j<num;j++)
        {
            if(min>a[j])
            {
                min=a[j];
                k=j;
            }
        }

        temp=a[i];
        a[i]=a[k];
        a[k]=temp;
    }

    printf("\nThe Sorted list is \n");
    for(i=0;i<num;i++)
    {
        printf("%d ",a[i]);
    }

    return 0;
}

