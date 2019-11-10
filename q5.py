import math

r1,r2,d,x1,x2 = map(int, input().split())

a = (math.pi*r1*x1)/2
b = (math.pi*r2*x2)/2

nd = d+ abs(b-a)


case = x1%4
ans = 0

if case == 0 :
    if x2%4 == 0 or x2%4 == 2:
        dia = 2*r2
        ans = math.degrees(math.atan(dia/nd))
        
    if x2%4 == 1 or x2%4 == 3:
        d1 = nd - r2
        d2 = nd + r2
        
        val1 = math.atan(r2/d1)
        val2 = math.atan(r2/d2)
        
        ans = math.degrees(val1 -val2)
        
elif case == 1 :
    if x2%4 == 0 or x2%4 == 2:
        dia = nd + r1
        
        val1 = math.atan(dia/r1)
        r = 2*r2 - r1
        val2 = math.atan(dia/r)
        
        ans = 180 - math.degrees(val1 + val2)
        
    if x2%4 == 1 or x2%4 == 3:
        d1 = nd - r2
        d2 = nd + r2
        
        r = r2-r1
        val1 = math.atan(r/d1)
        val2 = math.atan(r/d2)
        
        ans = math.degrees(val1 -val2)
        
        
elif case == 2 :
    
    if x2%4 == 0 or x2%4 == 2:
        
        val1 = math.atan(nd/(2*r1))
        val2 = math.atan(nd/(2*r2 - 2*r1))
        
        ans = 180 - math.degrees(val1+val2)
 
    if x2%4 == 1 or x2%4 == 3:
        
        r = abs(2*r1 - r2)
        
        d1 = nd - r2
        d2 = nd + r2
        
        val1 = math.atan(r/d1)
        val2 = math.atan(r/d2)
        
        ans = math.degrees(val1 - val2)
        
elif case == 3:
    
    if x2%4 == 0 or x2%4 == 2:
        
        dia = nd - r1
        
        val1 = math.atan(dia/r1)
        val2 = math.atan(dia/((2*r2)-r1))

        ans = 180 - math.degrees(val1+val2)
        
    if x2%4 == 1 or x2%4 == 3:
        
        r = r2-r1
        
        d1 = nd - r2
        d2 = nd + r2
        
        val1 = math.atan(r/d1)
        val2 = math.atan(r/d2)
        
        ans = math.degrees(val1-val2)
        
        
print("%.6f" %ans)        