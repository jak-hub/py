def sort(list):
    for i in range(len(list)):
        for j in range(i):
            if list[i]>list[j]:
                #print(i)
                t=list[i]
                list[i]=list[j]
                list[j]=t
            else:
                pass
    return list



list=[45,12,13,65,98,10,23]
sort(list)
print(list)