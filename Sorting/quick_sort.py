# Quicksort is a sorting algorithm that uses the concept of Divide and Conquer. 
# It effectively divides the array into partitions based on a pivot. (first element, last element or a random one)
# then it keeps swapping the elements till we get all smaller elemnts to the left of pivot and 
# larger elements to the right of pivot. this process is carried out recursively

# method for doing Quicksort
def quicksort(array, begin=0, end=None):
    if len(array) == 1:
        return array
    # first pass
    if end is None:
        end = len(array) - 1
    # stop clause
    if begin >= end:
        return
    # find the pivot by calling partition logic
    pivot = partition(array, begin, end)
    # sort elements for the partition before the pivot
    quicksort(array, begin, pivot-1)
    # sort elements for the partition after the pivot
    quicksort(array, pivot+1, end)

# partition logic 
def partition(array, begin, end):
    #considering the first element as pivot
    pivot = begin
    for current in range(begin+1, end+1):
        # if current element is smaller than or equal to first element
        # increment pivot by one and swap with current element
        if array[current] <= array[begin]:
            pivot += 1
            array[current], array[pivot] = array[pivot], array[current]
    # swap first element and pivot
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

#Input method
if __name__=='__main__':
    input_list = [2,5,6,5,34,11,23,0,3]
    quicksort(input_list)
    print(input_list)
