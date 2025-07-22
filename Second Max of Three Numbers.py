t=int(input())
while t > 0:
    ls=list(map(int, input().split()))
    r=max(ls)
    l=[]
    for i in ls:
        if i != r:
           l.append(i)
    print(max(l))
    t-=1
