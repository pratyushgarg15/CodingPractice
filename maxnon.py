def maxNonAdjacentSum(arr, size):
    inc = arr[0]
    excl = 0
    
    for i in range(1,size):
        temp = inc
        inc = excl + arr[i]
        excl = max(temp,excl)
        
    return max(inc,excl)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = list(map(int,input().strip().split()))[:size]
        print(maxNonAdjacentSum(arr,size))