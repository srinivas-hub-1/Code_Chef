T=int(input())
while T > 0:
    x,y=map(int, input().split())
    print(abs(x-y))
    T-=1
