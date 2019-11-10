#code
def rollingHash(s,p,alpahbet):
    
    if(len(p) > len(s)):
        print('-1')
        return
        
    patHash = 0
    
    flag = 0
    
    for char in p:
        patHash += alphabet[char]
        
    Hash = 0
    initial  = 0
    
    for i in range(len(p)):
        Hash += alphabet[s[i]]
    
    if Hash == patHash :
        print(s[0:len(p)], initial)
        flag += 1
        
    initial += 1
    
    for i in range(len(p), len(s)):
        Hash -= alphabet[s[initial-1]] 
        Hash += alphabet[s[i]]
        if(Hash == patHash):
            print(s[initial:i+1], initial)
            flag += 1
            
        initial += 1    
            
    if(flag == 0):
        print('-1')

t = int(input())
alphabet = {chr(i+96) : i for i in range(1,27)}

for i in range(t):
    s = input()
    p = input()
    
    rollingHash(s,p,alphabet)
            