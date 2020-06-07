for t in range(int(input())):
    x=int(input())
    arr=[i for i in bin(x)]
    c=0
    for k in range(2,len(arr)):
        if arr[k]=="1":
            c=c+1
    print(c)
            
