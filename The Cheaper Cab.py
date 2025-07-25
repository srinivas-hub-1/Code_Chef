T=int(input())

while T > 0 :
    x,y=map(int , input().split())
    
    if  x > y:
        
        print("Second")
        
    elif x==y:
        
        print("Any")
        
    else:
        
        print("First")
        
    T-=1
