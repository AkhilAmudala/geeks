def arrToBst(arr,low,high):
    if low>high:
        return
    mid = (low+high)//2
    print(arr[mid],end=" ")# root node
    arrToBst(arr,low,mid-1)# left
    arrToBst(arr,mid+1,high)# right

if __name__=='__main__':
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        arrToBst(arr,0,n-1)
        print()
