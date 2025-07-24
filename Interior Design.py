T=int(input())
while T > 0 :
    x,y,z,v=map(int , input().split())
    print(min((x+y),(z+v)))
    T-=1
