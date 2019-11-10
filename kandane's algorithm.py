# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 13:27:53 2018

@author: HP
"""

# Python program to find maximum contiguous subarray
 
def maxSubArraySum(arr,size):
     
    max_so_far =arr[0]
    curr_max = arr[0]
     
    for i in range(1,size):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far

def circularArrayKadane():
    
    pass
 
# Driver function to check the above function 
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is" , maxSubArraySum(a,len(a)))
 