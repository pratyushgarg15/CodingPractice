# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:09:15 2019

@author: HP
"""

def isPrime(n):
    if(n<=1):
        return False
    if(n<=3):
        return True
    
    if(n%2 == 0 or n%3 == 0):
        return False
    i = 5
    
    while(i*i <= n):
        if(n%i == 0 or n%(i+2) == 0):
            return False
        i+=6
        
    return True


print(isPrime(5))