# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 00:37:16 2019

@author: HP
"""

def coinChangeRecursive(coins, m, total):
    if(total == 0):
        return 1
    
    if(total < 0):
        return 0
    
    if(total>=0 and m<=0):
        return 0
    
    return coinChangeRecursive(coins,m-1,total)+ coinChangeRecursive(coins,m,total-coins[m-1])
              

def coinChangeDP(coins, m, total):
    table = [[1]*(total+1)]*m
    
    for row in range(len(table)):
        for col in range(1,len(table[0])):
            if(col - coins[row]>=0):
                x = table[row][col-coins[row]]
            else:
                x = 0
                
            if(row > 0):
                y = table[row-1][col]
            else:
                y = 0
                
            table[row][col] = x + y
            
    return table[len(table)-1][len(table[0])-1]        
    

              

if __name__ == '__main__':
    coins = [1,3,5]
    total = 1000
    m = len(coins) 
    print(coinChangeDP(coins, m, total))
    