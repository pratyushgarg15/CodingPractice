# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 23:12:03 2019

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
    
def nthPrime(n):
    if(n == 1):
        return 2
    if(n == 2):
        return 3
    
    count = 2
    num = 6
    
    while(count!=n):
        if isPrime(num - 1):
            count += 1
        
        if(count == n):
            return num-1
        
        if isPrime(num + 1):
            count += 1
          
        if(count == n):
            return num+1    
            
        num += 6 
            
if __name__ == '__main__':
    for i in range(1,100):
        print(i,".  ",nthPrime(i),sep = '')        
            
        