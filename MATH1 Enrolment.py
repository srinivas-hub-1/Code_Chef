T=int(input())
while T > 0:
    x,y=map(int,input().split())
    if x > y:
        print("0")
    else:
        print(y-x)
    T-=1
