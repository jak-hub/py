"""lst=[2,5,8,9,7,11,21,13,17]
p_lst=[]
count=0
prime=0
for i in lst:
    s=i
    for j in range(1,i+1):
        r=(int)(s%j)
        #print(r)
        if r==0:
            count+=1
        else :
            pass
    if count==2:
        prime+=1
        p_lst.append(s)
        count=0
    else:
        count=0

print(prime,'\n',p_lst)"""

n=int(input("enter the prime range:"))
p_lst=[]
count=0
prime=0
for i in range(1,n+1):
    s=i
    for k in range(1,i+1):
        r=(int)(s%k)
        if r==0:
            count+=1
        else:
            pass
    if count==2:
        p_lst.append(s)
        count=0
        prime+=1
    else:
        count=0

print(prime,"\n",p_lst)




