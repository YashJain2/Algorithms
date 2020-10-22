//contributed by @swati-gwc aka Swati Tripathi
// Implementing Quick Sort in Java
import java.io.*;
import java.util.Scanner;
public class PractiseJava {

   
     /* Here last element of input array is taken as the pivot
       ans the below function will place the pivot from last index 
       to its correct position i.e. pivot will be placed at index 
       where elements left to pivot are smaller in value than pivot 
       and elements right to pivot in array are greater in value than pivot
       value*/
    int partition(int array[], int first, int last) 
    { 
        int pivot = array[last]; //last element is the pivot
        int i = (first-1); // index of smaller element 
        for (int j=first; j<last; j++) 
        { 
            // If current element is smaller than the pivot
            //then following if statement is executed
            if (array[j] < pivot) 
            { 
                i++; 
  
                // swapping the values of  arr[i] and arr[j] 
                int temp = array[i]; 
                array[i] = array[j]; 
                array[j] = temp; 
            } 
        } 
  
        // swap arr[i+1] and arr[high] (or pivot) 
        int temp = array[i+1]; 
        array[i+1] = array[last]; 
        array[last] = temp; 
  
        return i+1; 
    } 
  
  
    /* The function below implements QuickSort() and here
      array[] : Array to be sorted, 
      first  : first index, 
      last : last index
      Note: This is a recursive function*/
    void sort(int array[], int first, int last) 
    { 
        if (first < last) 
        { 
            /* part is the partitioning index, array[part] is  
              now at right place */
            int part = partition(array, first, last); 
  
            // Recursively sort elements before 
            // partition and after partition 
            sort(array, first, part-1); 
            sort(array, part+1, last); 
        } 
    } 
  
    /* Function to print array */
    static void printfunc(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    // Main function of this program
    public static void main(String args[]) throws IOException 
    { 
       
  
        System.out.println("Enter the size of array you wish to enter: "); 
        //to accept array size from user
       // BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
        Scanner sc =new Scanner(System.in);
        //create an int type array
        int n= sc.nextInt();
        int arr[] = new int[n];
        
        //accept integer elements into array
        System.out.println("Enter elements of array");
        for(int i=0;i<n; i++)
        {
            
            arr[i] = sc.nextInt();
        }
        
 
        PractiseJava ob = new PractiseJava(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("Final sorted array is:"); 
        printfunc(arr); 
    } 
    
}
/* Output of this code will be as follows:
Enter the size of array you wish to enter: 
5
Enter elements of array
99 0 -12 3 23
Final sorted array is:
-12 0 3 23 99 
*/