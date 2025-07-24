T=int(input())
while T > 0 :
    x,y,z=map(int , input().split())
    if x*y <= z:
        print("yes")
    else:
        print("No")
    T-=1
