from array import *

ar=array('i',[])

n=int(input("ENTER THE LENGTH:"))

for i in range(n):
    a=int(input("ENTER THE ARRAY"))
    ar.append(a)

print(ar)

f=int(input("ENTER THE INDEX U WANT TO KNOW:"))

for j in range(len(ar)):
    if f==j:
        e=ar[j]
    else:
        pass

print("THE NUMBER FROM THE INDEX U MENTION IS:\t",end="")
print(e)
print(ar.index(f))