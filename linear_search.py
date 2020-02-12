def search(list,n):
    for i in range(len(list)):
        #print(i,n,end="")
        #print(i)
        if list[i]==n:
            return True,i
        else:
            pass
    else:
        return False,0

list=list(range(1,10+1))
print(list)
T,Q=search(list,99)
#print(list)
if T==True:
    print("Found",Q+1)
else:
    print("NOT",Q)