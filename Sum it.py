# cook your dish here
t=int(input())
while t > 0:
    x,y,c=map(int,input().split())
    if x+y==c:
       print("yes")
    else:
         print("No")
    t-=1
