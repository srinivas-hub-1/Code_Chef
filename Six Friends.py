T=int(input())
while T > 0:
    x,y=map(int , input().split())
    print(min((x*3),(y*2)))
    T-=1
