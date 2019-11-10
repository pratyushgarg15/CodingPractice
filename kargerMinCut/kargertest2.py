# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:14:24 2019

@author: HP
"""
import random 

cuts=[]
def kargerMinCut(graph):
    while len(graph) > 2:
         v = random.choice(list(graph.keys()))
         w = random.choice(graph[v])
         contract(graph, v, w)
    mincut = len(graph[list(graph.keys())[0]])
    cuts.append(mincut)
def contract(graph, v, w):
    for node in graph[w]:  # merge the nodes from w to v
         if node != v:  # we dont want to add self-loops
             graph[v].append(node)
         graph[node].remove(w)  # delete the edges to the absorbed 
         if node != v:
              graph[node].append(v)
    del graph[w]  # delete the absorbed vertex 'w'