/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

public class Main
{
	void selection_sort(int arr[])
    {
        int n = arr.length;
 
        // One by one moveing the boundary of unsorted subarray
        for (int i = 0; i < n-1; i++)
        {
            // to find the minimum element in the unsorted subarray
            int min_idx = i;
            for (int j = i+1; j < n; j++)
                if (arr[j] < arr[min_idx])
                    min_idx = j;
 
            // Swap the found minimum element with element prensent at the boundary
            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
    }
 
    //to print the array
    void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i]+" ");
        System.out.println();
    }
 
    // Driver code to test above
    public static void main(String args[])
    {
        Main ob = new Main();
        int arr[] = {2,5,6,5,34,11,23,0,3};
        ob.selection_sort(arr);
        System.out.println("Sorted array");
        ob.printArray(arr);
    }
}
/*Output:

Before Selection Sort
2 5 6 5 34 11 23 0 3 
After Selection Sort
0 2 3 5 5 6 11 23 34
*/
