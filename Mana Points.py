T=int(input())
while T > 0:
    x,y=map(int , input().split())
    print(int( y //x ))
    T-=1
