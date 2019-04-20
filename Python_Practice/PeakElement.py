# Given an array A of integers. The task is to find a peak element in it.
# An array element is peak if it is not smaller than its neighbors. For corner elements, we need to consider only one neighbor. 

# returns the index of peak element

def peakElement(arr, n):
    return findPeak(arr,0,n-1,n)

def findPeak(arr,low,high,n):
    mid = low + (high-low)/2
    mid = int(mid)
    
    if ((mid == 0 or arr[mid-1] <= arr[mid]) and (mid == n-1 or arr[mid+1]<= arr[mid])):
        return mid
        
    elif (mid > 0 and arr[mid-1] > arr[mid]):
        return findPeak(arr,low,(mid-1),n)
    
    else:
        return findPeak(arr,(mid+1),high,n)
