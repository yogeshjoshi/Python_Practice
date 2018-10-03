if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxElement = max(arr)
    while maxElement == max(arr):
        arr.remove(maxElement)
    print(max(arr))
        
        
       