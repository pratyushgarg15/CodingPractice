# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 00:49:02 2019

@author: Acer
"""

def printnum1(mat, end_row, end_col, start_row, start_col):
    
    for col in range(start_col,end_col):
        print(mat[start_row][col])
        
    for row in range(start_row+1,end_row):
        print(mat[row][col])

def printnum2(mat, end_row, end_col, start_row, start_col):        
    
    for col in range(end_col-1,start_col-1,-1):
        print(mat[end_row][col])
        
    for row in range(end_row-1,start_row,-1):
        print(mat[row][col])    
        

mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]    
#mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
end_row = len(mat)
end_col = len(mat[0])

start_row = 0
start_col = 0

while(end_row > start_row and end_col > start_col):

    printnum1(mat, end_row, end_col, start_row, start_col)

    end_row -=1
    end_col -=1
    
    if(end_row <= start_row or end_col <= start_col):
        break

    printnum2(mat, end_row, end_col, start_row, start_col)

    start_row += 1
    start_col += 1

    