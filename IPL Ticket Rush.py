T= int(input())
while T > 0:
    x,y=map(int , input().split())
    if  x < y:
        print("0")
    else:
        print(x-y)
    T-=1
