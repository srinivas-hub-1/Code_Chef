t=int(input())
while t > 0:
    x,y=map(int , input().split())
    if x > y:
        print("Loss")
    elif x==y:
        print("Neutral")
    else:
        print("profit")
    t-=1
