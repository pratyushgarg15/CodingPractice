import sys
from queue import PriorityQueue

def dijkstra(graph,source):
    dist = [sys.maxsize]*(len(graph)+1)
    dist[source] = 0
    Q = PriorityQueue()
    Q.put([0,source])
    settled = set()
    count = 0
    
    while not Q.empty():
        v = Q.get()[1]
        settled.add(v)
        #print(len(settled),end = '\t')
        
        for neighbour in graph[v]:
            u = neighbour[0]
            if u not in settled:
                print(u,end = '\t')
                length = neighbour[1]
                altDist = dist[v] + length
            
                if altDist < dist[u]:
                    dist[u] = altDist 
                    Q.put([dist[u],u])
                    
        count += 1 

    print(count)         
    
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