from collections import defaultdict

def scc():
    pass



if __name__ == '__main__':
    revGraph = defaultdict(list)
    graph = defaultdict(list)
    
    with open('SCC.txt','r') as file:
        line = file.readline()
        while(line):
            head , tail = map(int , line.strip('\n').split())
            graph[head].append(tail)
            revGraph[tail].append(head)
            line = file.readline()

    print(graph[10])