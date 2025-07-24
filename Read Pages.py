T=int(input())
while T > 0:
    x,y,z=map(int, input().split())
    if y * z >= x:
        print("Yes")
    else:
        print("No")
    T-=1
