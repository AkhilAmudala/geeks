
#didnt get logic

for t in range(int(input())):
    k,n=map(int,input().split(" "))
    arr=[i for i in input().split(" ")]
    arrout=[]
    for j in range(k,n):
        arr=arr[:j]



#############
    k, n = [int(x) for x in input().split()]
    lst = [int(x) for x in input().split()]
    res = [-1]*(k-1)
    ans = []
    yo = []
    for j in range(k,n+1):
        yo = lst[:j]
        yo.sort()
        ans.append(yo[j-k])
    jus = res+ans
    print(*jus,sep=" ")
