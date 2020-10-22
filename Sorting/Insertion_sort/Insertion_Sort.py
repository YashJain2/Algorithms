
#Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

def insertion_sort(input_list):

    # Sort the elements to arrange in order using Insertion Sort algorithm
    for i in range(1, len(input_list)): # Set the range to run the loop n times
        j = i - 1
        nxt_element = input_list[i]

        # Compare the current element with next element and sorting it
        while (input_list[j] > nxt_element) and (j >= 0):
            input_list[j + 1] = input_list[j]
            j = j - 1
            input_list[j + 1] = nxt_element


input_list = [2,5,6,5,34,11,23,0,3]
insertion_sort(input_list)
print(input_list)