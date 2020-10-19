
#Selection sort is a simple sorting algorithm. This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty and the unsorted part is the entire list.
#The smallest element is selected from the unsorted array and swapped with the leftmost element, and that element becomes a part of the sorted array. This process continues moving unsorted array boundary by one element to the right.

def selection_sort(input_list):

    for iteration_value in range(len(input_list)):

        min_iteration_value = iteration_value
        for i in range( iteration_value +1, len(input_list)):
            if input_list[min_iteration_value] > input_list[i]:
                min_iteration_value = i

        # Sort the least value with the compared value using Selection Sort Algorithm
        input_list[iteration_value],input_list[min_iteration_value] = input_list[min_iteration_value],input_list[iteration_value]


input_list = [2,5,6,5,34,11,23,0,3]
selection_sort(input_list)
print(input_list)