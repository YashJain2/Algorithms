
#Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

def bubblesort(input_list):

  # Sort the elements to arrange in order using Bubble Sort algorithm
        for iteration_value in range(len(input_list)-1,0,-1):

             for iteration_position in range(iteration_value):

                # Compare the current element with next element and sorting it
                if input_list[iteration_position]>input_list[iteration_position+1]:
                    temp = input_list[iteration_position]
                    input_list[iteration_position] = input_list[iteration_position+1]
                    input_list[iteration_position+1] = temp


input_list = [2,5,6,5,34,11,23,0,3]
bubblesort(input_list)
print(input_list)