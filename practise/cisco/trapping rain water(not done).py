
# use other logic --- i<i+1 and i<i-1
for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().strip().split()))
    m=sorted(set(arr))
    lst=[]
    for i in range(n-1):
        if(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
            lst.append(i)
    print(lst)
    sum=0
    for i in range(lst[0],n-1):
        l=m[-1]
        k=m[-2]

        #if(arr[i]>=k):
         #   sum+=0
        if(arr[i-1]>=arr[i]<=arr[i+1]):
            sum=sum + (min(arr[i+1],arr[i-1])-arr[i])
    print(sum)


#corret one :-by https://practice.geeksforgeeks.org/viewSol.php?subId=11909543&pid=281&user=VineetSharmat24

        x=[]
    for _ in range(int(input())):
        h=int(input())-1
        l=0
        a=list(map(int,input().split()));
        left_max=0
        right_max=0
        result=0
        while(l<h):
            if(a[l]<a[h]):
                if(a[l]>left_max):
                    left_max=a[l]
                else:
                    result+=left_max-a[l]
                l+=1
            else:
                if(a[h]>right_max):
                    right_max=a[h]
                else:
                    result+=right_max-a[h]
                h-=1
        x.append(result)
    for i in x:
        print(i)
            
