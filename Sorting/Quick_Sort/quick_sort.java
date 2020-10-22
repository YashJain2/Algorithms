import java.util.*;
import java.lang.*;
import java.io.*;

class QuickSortJava
{
    public static void main(String[] args)
    {
        int[] arr={1,6,9,3,23};
        QuickSortJava test1= new QuickSortJava();
        test1.sort(arr,0, (arr.length-1));
        for (int j : arr)
        {
            System.out.print(j + "\t");
        }
        //Output 1	3	6	9	23
    }

    public int partition(int [] arr, int first, int last)
    {
        int pivot = arr[last];
        int i = (first - 1);
        for (int j = first; j < last; j++)
        {
            if (arr[j] < pivot)
            {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i+1];
        arr[i+1] = arr[last];
        arr[last] = temp;

        return i+1;
    }

    public void sort(int [] arr, int first, int last)
    {
        if(first<last)
        {
            int p = partition(arr,first,last);

            sort(arr, first,p-1);
            sort(arr, p+1,last);
        }
    }

}