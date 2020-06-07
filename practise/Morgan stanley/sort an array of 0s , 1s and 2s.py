#use (*arr) takes 2.58 sec .... since we use sorted
for t in range(int(input())):
    x=int(input())
    arr=list(map(int,input().split()))
    arr1=sorted(arr)
    print(*arr1)


#since sorting takes time --------- use this method !! *awesome 0.95 sec
T = int(input())
while T:
    N = int(input())
    arr = [*map(int, input().split())]
    print(arr.count(0)*"0 " + arr.count(1)*"1 " + arr.count(2)*"2 ")
    arr.clear()
    T -= 1

# next test case in the same line
for t in range(int(input())):
    x=int(input())
    arr=list(map(int,input().split(" ")))
    arr1=sorted(arr)
    for k in range(x):
        print(arr1[k],end=" ")
