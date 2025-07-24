T=int(input())
while T > 0 :
    x,y=map(int , input().split())
    if x >=  y*2:
        print("Yes")
    else:
        print("No")
    T-=1
