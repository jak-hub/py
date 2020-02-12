p=0
def search(list,n):
    a=(int)(len(list))
    b=(int)(0)
    c=(int)(2)
    for i in range(len(list)):
        d=(int)((b+a)/c)
        if list[d]==n:
            globals()['p']=d
            return True
        else:
            if list[d]<n:
                b=(int)(d)
                print("L")
            else:
                a=(int)(d)
                print("U")
    else:
        return False




list=list(range(1,25,2))
print(list,len(list))
if search(list,11):
    print("FOUND\n","pos-",end="")
    print(p+1)
else:
    print("NOT\n","pos-",end="")
    print(p)