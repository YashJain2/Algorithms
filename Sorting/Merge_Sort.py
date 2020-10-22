#Merge Sort - a way of sorting, which uses divide and conquer method.

def merge_sort(values): 

	# Splitting of list into approximately two equal halves
	if len(values)>1: 
		m = len(values)//2  

		# Splitting left and right sublists
		left = values[:m] 
		right = values[m:] 

		# Recrusive call to merge_sort to do the same process for the available sublist
		left = merge_sort(left) 
		right = merge_sort(right) 

		values =[] 

		# Comparing the first elements of both sublists and appending the lowest of two to "values" list
		# list.pop(0) => removes the first element (0th index) of list
		while len(left)>0 and len(right)>0: 

			# condition that, left sublist element is lesser than that of right
			if left[0]<right[0]: 
				values.append(left[0]) 
				left.pop(0)

			# condition that, right sublist element is greater than or equal to that of left
			else: 
				values.append(right[0]) 
				right.pop(0) 

		# Assuming that either of the list becomes null, where other still has elements in it
		# Left sublist has elements, Right sublist is null
		for i in left: 
			values.append(i) 

		# Right sublist has elements, Left sublist is null
		for i in right: 
			values.append(i) 
	
	# After appending the sorted order, the list is returned to the position, where it was called recently
	return values 


# Input - list
a = list(map(int, input("Enter space-splitted values: ").split(' ')))
print("Given array is") 
print(a) 

# Calling the function which performs merge sort
a = merge_sort(a) 

# Output
print("Sorted array is : ") 
print(a) 

'''Expected Input/Output:
 Input: [5, 3, 12, 8, 7, 9]
Output: [3, 5, 7, 8, 9, 12]
'''
