# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:22:41 2019

@author: HP
"""
count = 0

def partition(arr, l, r):
    global count
    pivot = arr[r]
    i = l
    for j in range(l,r):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1
            count+=1
    arr[r], arr[i] = arr[i], arr[r]        
    return i
    
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