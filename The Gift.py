x,y,z=map(int , input().split())
r1= abs(y- z)
r2=r1+x
if  r2 >= y:
    print("Yes")
else:
    print("No")
