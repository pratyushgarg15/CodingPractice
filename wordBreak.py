# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:28:57 2019

@author: HP
"""

def dictContains(substr):
    dictionary = ['snake', 'snakes', 'sand', 'and', 'ladder']
    if substr in dictionary :
        #print(substr)
        return True
    else:
        return False
    
def wordBreakRecursive(string):
    print(string)
    if len(string) == 0:
        return True
    
    for i in range(1,len(string)):
        if(dictContains(string[0:i]) and wordBreakRecursive(string[i:len(string)-i])):
            return True
            
    return False
        
        
if __name__ == '__main__':
    string = input()
    print(wordBreakRecursive(string))        