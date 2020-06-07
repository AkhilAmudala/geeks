#0.51 sec
def equ(arr):
    if(len(arr)==1):
        print(1)
    else:
        l=0
        r=0
        r=sum(arr)
        for i in range(0,len(arr)):
            r-=arr[i]
            if(l==r):
                print(i+1)
                return
            l+=arr[i]
        print(-1)
for i in range(0,int(input())):
    n=int(input())
    arr=[*map(int,input().split())]
    equ(arr)




# time taking > 2.28 sec !!!!!! danger
t=int(input())
while t:
    n=int(input())
    arr=[*map(int,input().split())]

    if(len(arr)==1):
        print("1")
    if(len(arr)>1):
        s=0
        for i in range(n):
            if(sum(arr[:i])==sum(arr[i+1:])):
                print(i+1)
                break
        else:
            print(-1)
    t-=1
