def isValid(s):
    freq=[0]*26

    for i in range(len(s)):
        freq[ord(s[i])-97]+=1

    a = {}    

    for num in freq:
       if(num > 0):
           if num in a:
               a[num] += 1
           else:
               a[num] = 1

    print(a)

    if(len(a)>2):
        return "NO"
    elif(len(a) == 1 ):
        return "YES"
    else:
        keys = list(a.keys())
        values = list(a.values())
        b = abs(keys[0]-keys[1])
        if(b>1):
            c = True if keys[0] == 1 and values[0] == 1 else False
            c = True if keys[1] == 1 and values[1] == 1 else False
            if(c):
                return "YES"
            else:
                return "NO"
        else:
            if(values[0] == 1 or values[1] == 1):
                return "YES"
            else:
                return "NO"
            
        
            

if __name__ == '__main__':
    with open('inputString.txt' , 'r') as file:
        s = file.read().replace('\n','')         
        
    print(isValid(s))