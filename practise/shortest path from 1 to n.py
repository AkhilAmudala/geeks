def getShortest(n):
    edge = 0
    while n != 1:
        if n % 3 != 0:
            n -= 1
        else:
            n = n // 3
        edge += 1
    return edge
    
t = int(input())
for i in range(t):
    n = int(input())
    print(getShortest(n))

            
            
