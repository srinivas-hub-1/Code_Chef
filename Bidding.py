T=int(input())
while T > 0:
    a,b,c=map(int , input().split())
    if a > b and a > c :
        print("Alice")
    elif b>c and b>a:
        print("Bob")
    else:
        print("charlie")
    T-=1
