T=int(input())

while T > 0 :
    x=int(input())
    
    if x <= 3:
        
        print("Bronze")
        
    elif x >= 3 and x <= 6:
        
        print("Silver")
    
    else:
        print("Gold")
        
    T-=1
