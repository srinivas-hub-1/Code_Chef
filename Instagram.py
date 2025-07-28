T=int(input())
 
for _ in range(T):
    x,y=map(int , input().split())
    
    if x > y*10:
        
        print(" Yes ")
        
    else:
        
        print(" No ")
