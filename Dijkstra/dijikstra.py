import sys

def minimum(dist,visited):
    minim = sys.maxsize
    
    for i in range(1,len(dist)):
        if(visited[i] == False and dist[i]<minim):
            minim = i
            
    return minim        

def dijkstra(graph,source):
    dist = [sys.maxsize]*(len(graph)+1)
    dist[source] = 0
    Q = {i for i in range(1,len(graph)+1)}
    visited = [False]*(len(graph)+1)
    
    while len(Q) != 0:
        v = minimum(dist, visited)
        
        Q.remove(v)
        visited[v] = True
        #print(v)
        
        for neighbour in graph[v]:
            u = neighbour[0]
            if u in Q :
                length = neighbour[1]
                altDist = dist[v] + length
            
                if altDist < dist[u]:
                    dist[u] = altDist 
    
    return dist

if __name__ == '__main__':
    graph = {}
    vertex = 1
    with open('dijkstraData.txt','r') as file:
        line = file.readline()
        while(line):
            l = [val for val in line.split('\t') if (val != '\n' and val != '')]
            l = list(map(lambda s: s.split(','), l[1:]))
            l = [[int(j) for j in i]for i in l]
            graph[vertex] = l
            vertex += 1
            line = file.readline()
            
    #print(graph)

   
    dist = dijkstra(graph, 1)
    
    '''for i,val in enumerate(dist):
        print(f'{i} = {val}')'''
        
    print(dist[7],dist[37],dist[59],dist[82],dist[99],dist[115],dist[133],dist[165],dist[188],dist[197],sep =',')    