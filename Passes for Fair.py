T=int(input())
for _ in range (T):
    x,y=map(int , input().split())
    if y > x:
        print("yes")
    else:
        print("No")
    T-=1
