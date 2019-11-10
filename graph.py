# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:26:45 2019

@author: HP
"""

from collections import deque


class Graph:

    def __init__(self , vertices):
        self.vertices = vertices
        self.g = {}
        for i in range(0, vertices):
            self.g[i] = []
        
    def addEdge(self , src , dest):
        self.g[src].append(dest)
        
    def printGraph(self):
        print(self.g)
        print(self.g.keys())
        for key,items in self.g.items():
            print(key,end = '')
            for i in items:
                print('->',i,sep = '',end = '')
            print()
                      
            
    def bfs(self,s):
        queue = deque()
        visited = [False]*self.vertices
        queue.append(s)
        visited[s] = True
        
        while (len(queue)):
            vertex = queue.popleft()
            for node in self.g[vertex]:
                if(not visited[node]):
                    visited[node] = True
                    queue.append(node)  
            
            print(vertex, end = ' ')
                    
            
    def dfs(self,s):
        
        stack = deque()
        visited = [False]*self.vertices
        stack.append(s)
        visited[s] = True
        
        while(len(stack)):
            vertex = stack.pop()
            for node in self.g[vertex]:
                if(not visited[node]):
                    visited[node] = True
                    stack.append(node)
                    
            print(vertex, end = ' ')  
            
    def topological_sort(self):
        stack = deque()
        result = []
        visited = [False]*self.vertices
        
        for vertex in range(self.vertices):
            if (not visited[vertex]):
                stack.append(vertex)
                visited[vertex] = True
                while(len(stack)):
                    node = stack.pop()
                    
                    for v in self.g[node]:
                        if (not visited[v]):
                            visited[v] = True
                            stack.append(v)
                            result.insert(0,v)
                result.insert(0,vertex)
        for i in result:
            print(i , end = ' ')
        
        
                
if __name__ == '__main__':
    g= Graph(6) 
    g.addEdge(5, 0); 
    g.addEdge(5, 2); 
    g.addEdge(4, 0); 
    g.addEdge(4, 1); 
    g.addEdge(2, 3); 
    g.addEdge(3, 1); 
    
    g.printGraph()
    
    '''g.bfs(5)
    print()
    g.dfs(5)
    print()'''
    g.topological_sort()