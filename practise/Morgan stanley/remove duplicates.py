def remove_duplicate(n, arr):
    for i in arr:
        for k in range(arr.count(i)-1):
            arr.remove(i)
    return len(arr)#taken this len as 'n' in driver

#driver code given in question
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[*map(int,input().strip().split())]
        n=remove_duplicate(n,arr)#'get this'
        for i in range(n):
            print(arr[i],end=" ")
        print()



