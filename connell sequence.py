n = int(input())

numberOfTimes = 0
num = 0
while(n):
    numberOfTimes += 1
    num -= 1
    for i in range(numberOfTimes):
        num += 2
        print(num, end = ' ')
        n -= 1
        if(n == 0):
            break
        
        