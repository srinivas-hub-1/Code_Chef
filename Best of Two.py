t=int(input())
while t > 0:
    x,y=map(int, input().split())
    print(max(x,y))
    t-=1
