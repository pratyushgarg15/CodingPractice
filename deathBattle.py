t = int(input())
for i in range(t):
    a,h,l1,l2,m,c = map(int, input().strip().split())
    luck = l1/l2
    superAttack = a*c
    
    if(superAttack*m < h):
        print("RIP")
    