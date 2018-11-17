def minimum2(): # Python code to find second minimum number in array, time complexity O(N)
    arr = [1,3,4,0,7,9]
    min1 = 10000 # Just taking maximum number (random)
    min2 = 10000
    for i in range(0,len(arr)):
        if arr[i]<min1: 
            # print('---')
            min2 = min1
            min1 = arr[i]
        if arr[i]>min1 and arr[i]<min2:
            # print('+++')
            min2 = arr[i]
    print(min1) # minimum number in the array
    print(min2) # second minimium number in the array

minimum2()
