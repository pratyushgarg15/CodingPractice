# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 00:30:35 2019

@author: HP
"""

def result(n,r):
    fact = [1]*(n+1)
    
    for i in range(1,n+1):
        fact[i] = fact[i-1]*i
        
    ''' formula = nCr*(p)^r*(1-p)^(n-r)'''
    
    res = fact[n]/(fact[r]*fact[n-r])
    
    res *= 0.5**r * 0.5**(n-r)
    
    return res


if __name__ == '__main__':
    n = int(input("Enter value of n : "))
    r = int(input("Enter value of r : "))
    
    print(result(n,r))
    
    