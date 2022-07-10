#!/bin/python3


print("Python  script for binary search.")

def binary_search(arr, n ,k):
    start = 0
    end = n-1
    

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            end = mid - 1
        else:
            start = mid + 1


    return None


if __name__ == '__main__':
    n = int(input())
    arr=list(map(int, input().split(' ') ))
    
    k = int(input())

    ans=binary_search(arr, n, k)
    print("Found at: ",ans)