import sys

#n^2 complexity
def maxIndex(arr, n):
    maxDiff = -sys.maxsize
    
    for i in range(n-1):
        for j in range(n-1,i-1,-1):
            if(arr[i]>arr[j] and maxDiff < j-i):
                maxDiff = j-i
                break 
    return maxDiff

def maxIndex2(arr, n):
    leftMax = [0 for i in range(n)]
    rightMin = [0 for i in range(n)]
    
    leftMax[0] = arr[0] 
    for i in range(1, n): 
        leftMax[i] = max(arr[i], leftMax[i - 1]) 
  
    rightMin[n - 1] = arr[n - 1] 
    for j in range(n - 2, -1, -1): 
        rightMin[j] = min(arr[j], rightMin[j + 1]); 
  
    i, j = 0, 0
    maxDiff = -1
    while (j < n and i < n): 
        if (leftMax[i] > rightMin[j]): 
            maxDiff = max(maxDiff, j - i) 
            j = j + 1
        else: 
            i = i + 1
  
    return maxDiff 


if __name__=='__main__':
    arr = list(map(int, input().strip().split()))    
    
    print(maxIndex2(arr, len(arr)))