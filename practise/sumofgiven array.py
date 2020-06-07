for t in range(int(input())):
    n,a,b=map(int,input().split(" "))

    arr=[i for i in input().split(" ")]
    sum=0
    for j in range(a,b+1):
        sum+=arr[j]
    print(sum)
