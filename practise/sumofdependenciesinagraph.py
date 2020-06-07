#simply print e value
#error for other test cases?

from collections import Counter
for t in range(int(input())):
    n,e=map(int,input().split(" "))
    l=[i for i in input().split(" ")]
    x=[]
    for j in range(len(l)):
        if(j%2==0):
            x.append(l[j])
        s=dict((k,x.count(k)) for k in x)
    print(sum(s.values()))
