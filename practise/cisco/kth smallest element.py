t=int(input())
for i in range(t):
    x=int(input())
    arr1=[]
    arr=list(map(int,input().strip().split()))
    k=int(input())
    arr1=sorted(arr)
    print(arr1[k-1])
