# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:05:05 2019

@author: HP
"""
# Python program for implementation of MergeSort 
def mergeSort(arr, invcount): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements 
        R = arr[mid:] # into 2 halves 
        invcount = mergeSort(L, invcount) # Sorting the first half 
        invcount = mergeSort(R, invcount) # Sorting the second half 

        i = j = k = 0
		
		# Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
                
            else: 
                arr[k] = R[j] 
                j+=1
                invcount += len(L) - i
			
            k+=1
		
		# Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
		
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    
    return invcount
# Code to print the list 
def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i],end=" ") 
	print() 

# driver code to test the above code 
if __name__ == '__main__': 
    invcount = 0
    with open('input.txt') as f:
        arr = [int(i) for i in f]
    #print ("Given array is", end="\n") 
    #printList(arr) 
    invcount = mergeSort(arr,invcount) 
    #print("Sorted array is: ", end="\n") 
    #printList(arr) 
    print(invcount)

# This code is contributed by Mayank Khanna 
