t=int(input())
for k in range(t):
    n = int(input())
    arr = [int(i) for i in input().split(" ")] 
    sum = int(input())
    arrs=sorted(arr)
    def PairsCount(arr, n, sum):
            for i in range(0, n-1): 
                for j in range(i + 1, n): 
                    if (arr[i] + arr[j]) == sum:
                        print(str(arr[i]) + " " + str(arr[j]) +" " +str(sum))
            if arrs[-1]+arrs[-2] < sum:
                print(-1)

    PairsCount(arr, n, sum)
