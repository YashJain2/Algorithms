
class bubbleSort
{
public void optimizedBubbleSort(Integer[] arr) {
    int i = 0, n = arr.length;
    boolean swapNeeded = true;
    while (i < n - 1 && swapNeeded) {
        swapNeeded = false;
        for (int j = 1; j < n - i; j++) {
            if (arr[j - 1] > arr[j]) {
                int temp = arr[j - 1];
                arr[j - 1] = arr[j];
                arr[j] = temp;
                swapNeeded = true;
            }
        }
        if(!swapNeeded) {
            break;
        }
        i++;
    }
}
@Test
public void 
  givenIntegerArray_whenSortedWithOptimizedBubbleSort_thenGetSortedArray() {
      Integer[] array = { 2, 1, 4, 6, 3, 5 };
      Integer[] sortedArray = { 1, 2, 3, 4, 5, 6 };
      BubbleSort bubbleSort = new BubbleSort();
      bubbleSort.optimizedBubbleSort(array);
      assertArrayEquals(array, sortedArray);
}
