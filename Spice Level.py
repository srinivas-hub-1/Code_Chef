T=int(input())
while T > 0:
    x=int(input())
    if x < 4:
        print("MILD")
    elif x >= 4 and x < 7:
        print("Medium")
    else:
        print("Hot")
