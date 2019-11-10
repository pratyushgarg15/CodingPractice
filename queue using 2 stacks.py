# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 01:26:32 2019

@author: HP
"""

class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def peek(self):
        return self.stack1[0]
        
    def pop(self):
        self.stack2 = self.stack1[::-1]
        self.stack1.pop()
        self.stack2.pop()
        self.stack1[:] = self.stack2[::-1]
        
        
    def put(self, value):
        self.stack1.append(value)