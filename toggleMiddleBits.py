import math

t = int(input())

for i in range(t):
    num = int(input())
    a = 1
    n = math.floor(math.log2(num)+1)
    if(n%2 == 0):
        k = n//2
        m = num ^ (a<<k | a<<k-1)
        print(m)
    else:
        k = n//2
        m = num ^ (a<<k)
        print(m)