# Quicksort is a commonly used and efficient sorting algorithm developed by Tony Hoare in 1959.
# The worst case complexity is O(n^2) and average case complexity is O(n logn)
# When implemented well, it can be about two or three times faster than its main competitors, merge sort and heapsort


# This variation of quicksort selects last element as pivot.
def partition(arr, start, end):
    pivot = arr[end]

    # all elements till index low-1 are less than pivot
    low = start - 1        

    for i in range(start, end):
        
        if arr[i] < pivot:
            low += 1
            arr[low], arr[i] = arr[i], arr[low]

    arr[low+1], arr[end] = arr[end], arr[low+1]
    return low + 1



def quicksort(arr, start, end):
    if start >= end:
        return 
    
    # pivot arr[end] is put into correct position pvt
    pvt = partition(arr, start, end)

    # recurse for partitions
    quicksort(arr, start, pvt-1)
    quicksort(arr, pvt+1, end)



arr = [
        29, 99, 27, 41, 66, 28,
        44, 78, 87, 19, 31, 76, 
        58, 88, 83, 97, 12, 21, 44
       ]

quicksort(arr, 0, len(arr)-1)

print(*arr)