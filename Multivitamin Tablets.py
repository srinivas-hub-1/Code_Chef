T=int(input())
while T > 0 :
    x,y=map(int ,input().split())
    if x*3 <= y:
        print("Yes")
    else:
        print("No")
    T-=1 
