def quick_sort(arr,left,right):
    while left < right:
        mid = partition(arr, left, right)
        if((mid - left) < (right - mid)):
            quick_sort(arr, left, mid-1)
            left = mid + 1
        else:
            quick_sort(arr, mid+1, right)
            right = mid - 1
    return arr

def partition(arr,l,r):
    x = arr[l]
    j = l
    for i in range(l+1,r):
        if(arr[i] <= x):
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    left = 0
    right = n-1
    quick_sort(arr, left, right)
    print(arr)
