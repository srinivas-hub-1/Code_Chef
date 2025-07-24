T=int(input())
while T > 0 :
    x,y=map(int , input().split())
    if x <= y:
        print("No")
    else:
        print("Yes")
    T-=1
