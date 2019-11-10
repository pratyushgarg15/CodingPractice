# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 23:23:18 2019

@author: HP
"""

def isBalanced(s):
    stack = []

    if(s[0] == '}' or s[0] == ')' or s[0] == ']'):
        return 'NO'
    
    if(s[-1] == '{' or s[-1] == '[' or s[-1] == '('):
        return 'NO'

    for char in s:
        if(char == '{' or char == '(' or char == '['):
            stack.append(char)

        elif(char == ')' and len(stack)>0):
            if(stack[-1] == '('):   
                stack.pop()
            else:
                return 'NO'    
                
        elif(char == ']' and len(stack)>0):   
            if( stack[-1] == '['):   
                stack.pop()
            else:
                return 'NO' 
                
        elif(char == '}' and len(stack)>0):   
            if(stack[-1] == '{'):   
                stack.pop()
            else:
                return 'NO' 

        else:
            return 'NO'        
                
    if(len(stack)):
        return 'NO'

    return 'YES'  

print(isBalanced('[{}{})(]'))  

     