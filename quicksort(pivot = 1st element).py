# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:18:31 2019

@author: HP
"""

count = 0 

def partition(arr, l, r):
    global count
    pivot = arr[l]
    i = l+1
    count += r-l
    for j in range(l+1,r+1):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1
            
    arr[l], arr[i-1] = arr[i-1], arr[l]        
    return i-1
    
def quicksort(arr, l ,r):
    if(l<r):
        m = partition(arr, l, r)
        quicksort(arr, l, m-1)
        quicksort(arr, m+1, r)
        
        
if __name__ == '__main__':
    with open('quickSort_input.txt') as f:
        arr = [int(i) for i in f]
        #arr = arr[:200]
    quicksort(arr,0,len(arr)-1) 
    for num in arr:
        print(num,end=' ')
    print('\n',count)    