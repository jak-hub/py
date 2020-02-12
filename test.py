row=int(input("ENTER THE ROW: "))

for q in range(row):
    for s in range(1,row-q):
        print(" ",end="")
    for x in range(q+1):
        print("*",end="")
    for p in range(q):
        print("*", end="")
    #print("\r")
    print()

"""for i in range(row-2,-1,-1):
    for k in range(row-1-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for z in range(i):
        print("*", end="")
    #print("\r")
    print()"""