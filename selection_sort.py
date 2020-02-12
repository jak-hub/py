def sort(list):
   #print(len(list))
   for i in range(len(list)):
        m=i
        for j in range(i,len(list)):
            if list[m]<list[j]:
                m=j
            else:
                pass
        t=list[i]
        list[i]=list[m]
        list[m]=t







list=[45,12,13,65,98,10]
sort(list)
print(list)