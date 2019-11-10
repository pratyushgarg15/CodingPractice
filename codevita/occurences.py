if __name__ == '__main__':
    size = int(input())  
    s = input()
    t = int(input())
    
    l = [0]*len(s)
    h = {}
    
    h[s[0]] = 1
    
    for i in range(1,len(s)):
        if s[i] in h:
            l[i] = h[s[i]]
            h[s[i]] += 1
        else:
            h[s[i]] = 1
        

    for i in range(t):
        pos = int(input())
        print(l[pos-1])