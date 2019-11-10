list=[chr(97+i) for i in range(26)]
def superAscii(string):
    state=False
    for char in string:
        count=string.count(char)
        index=list.index(char)
        if(count==index+1):
            state=True
        else:
            state=False
            break
    if(state==True):
        return True
    else:
        return False


def minCost(string):
    ch=[]
    for char in string:
        if char not in ch:
            ch.append(char)        
    index=[]
    print(ch)
    for char in ch:
        ind=list.index(char)
        index.append(ind+1)
    length=sum(index)
    print(index)
    frequency=[]
    for char in ch:
        frequency.append(string.count(char))
    print(frequency)    
                
        
        
string=input("Enter the string : ")
if(superAscii(string)):
    cost=0
else:
    cost=minCost(string)
print(cost)
