import random

def contract(edge):
    global graph
    
    for vertex, edges in graph.items():
        for i in range(0,len(edges)):
            if(edges[i] == edge[1]):
                edges[i] = edge[0]
    
    l = graph[edge[0]]
    l.extend(graph[edge[1]])
    del graph[edge[1]]
    
    graph[edge[0]] = [x for x in graph[edge[0]] if x != edge[0]]
    
    print(edge[0],':',graph[edge[0]])
    #print(edge[1],':',graph[v2])
    
            

def random_edge():
    l = list(graph.keys())
    v1 = random.choice(l)
    v2 = random.choice(graph[v1])
    print(v1,v2)
    
    '''print(v1,':',graph[v1])
    print(v2,':',graph[v2])'''
    return (v1,v2)


n = 200 #number of vertices
graph = {}

with open("kargerMinCut.txt") as f:
    for i in range(0,n):
        l = [int(val) for val in f.readline().split('\t') if (val != '\n' and val != '')]
        graph[l[0]] = l[1:]
        
'''for k,l in graph.items():
    print(k,l)

for i in range(0,10):
    random_edge()'''


contract(random_edge())        

'''for k,l in graph.items():
    print(k,l)'''