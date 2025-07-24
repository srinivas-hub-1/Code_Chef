T=int(input())
while T > 0 :
    x=int(input())
    if  x < 3:
        print("Light")
    elif  x >= 3  and  x < 7:
        print("Moderate")
    else:
        print("Heavy")
    T-=1
