# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 13:44:04 2018

@author: HP
"""
import timeit

mysetup='''
from sympy import sieve
'''
mycode1='''
l=list(sieve.primerange(0, 100))
'''

mycode2='''
def sieve_of_eranthoses(n):
    n=1000000
    prime=[True for x in range(n+1)]
    p=2
    while(p*p<=n):
        if(prime[p]==True):
            for i in range(p*2,n+1,p):
                prime[i]=False
        p+=1
    for p in range(2,n):    
        if prime[p]:
            print(p)
'''            
            
print(timeit.timeit(stmt=mycode1,setup=mysetup,number=10000))            
print(timeit.timeit(stmt=mycode2,number=10000))       