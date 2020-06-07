
{
if __name__ == "main":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input.split()))
        b=list(map(int,input.split()))
        print(findExtra(a,b,n))
}


def findExtra(a,b,n):
    b.append(b[-1])
    for i in range(n):
        for j in range(n):
            if a[i]!=b[j] and i==j:
                return(i)
                break
