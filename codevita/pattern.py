def pattern(n,m,a,k,d,star):
    
    for i in range(n):
        print('*'*star,end='')
        star += 2
        for j in range(m):
            print(a*k,end='')
            k += 1
        for j in range(m):
            if(j != m-1):
                print(d+ 1*(j+1),'0',sep='',end='')
            else:
                print(d+ 1*(j+1))
            
        m = m-1
        d = d-m
    

if __name__ == '__main__':
    
    n = int(input())
    m = n
    star = 0 
    a = 10
    b = n*(n+1)/2
    c = n*(n-1)/2

    d = int(b+c) 
    k=1
    pattern(n,m,a,k,d,star)
            