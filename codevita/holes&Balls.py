nh = int(input())
dih = list(map(int, input().strip().split()))
nb = int(input())
dib = list(map(int, input().strip().split()))

count = [i+1 for i in range(nh)]

#print(nh,dih,nb,dib,count,sep='\n')



for i in range(nb):
    flag = False
    for j in range(nh-1,-1,-1):
        if(dib[i] <= dih[j] and count[j] != 0):
            print(j+1,end=' ')
            count[j] -= 1
            flag = True
            break
    if(flag == False):
        print('0',end = ' ')