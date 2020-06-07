for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    out=[-1]
    for j in range(1,n):
        c=arr[:j]
        cmax=max(c)
        cmin=min(c)
        if (cmin>arr[j]):
            out.append(-1)
        elif(cmax<arr[j]):
            out.append(cmax)
    print(*out,sep=" ")
