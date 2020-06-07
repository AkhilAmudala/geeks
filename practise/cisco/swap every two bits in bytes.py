for i in range(int(input())):
    a=list(bin(int(input())))
    print(a)
    if len(a)%2==1:
        a.insert(2,'0')
    a=a[2:]
    print(a)
    for j in range(0,len(a),2):
        a[j],a[j+1]=a[j+1],a[j]
    print(a)
    a=''.join(a)
    print(int(a,2))
