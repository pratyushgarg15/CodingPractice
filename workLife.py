t = int(input())
for i in range(t):
    n,k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    
    '''flag = False
    
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            flag = True
            break
       
    if(not flag):
        print(arr[-1])'''
        
    copy = arr[:]     
        
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            aux = arr[i]-arr[i+1]
            aux = aux//2
            if(aux<k):
                copy[i+1] += aux
                copy[i] -= aux
            else:
                copy[i+1] += k
                copy[i] -= k
                
    print(max(copy))         
        
        