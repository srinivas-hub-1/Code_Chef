t=int(input())

while t > 0:
    x,y=map(int , input().split())
    if x>=y:
        print("yes")
    else:
        print("No")
    t-=1
