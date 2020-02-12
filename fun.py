'''def mul(a,b):
	return (a*b)

def div(a,b):
	return (a/b)

def sub(a,b):
	return (a-b)

def add(a,b):
	return (a+b)

def mod(a,b):
	return (a%b)

def A_S_M_D_M(a,b):
	x=a+b
	y=a-b
	z=a*b
	u=a/b
	v=a%b

	return (x,y,z,u,v)

a=add(10,20)
b=sub(10,20)
c=mul(10,20)
d=div(50,5)
e=mod(15,3)

f,ad,cd,fg,hi=A_S_M_D_M(452,32)

print("a=",a,'\r',"b=",b,"\n","c=",c,"\n","d=",d,'\n',"e=",e,'\n',"f=",f,"ad",ad,"cd",cd,"fg",fg,"hi",hi)'''



'''def ls(lst):
	#lst=[10,20,31]
	lst[0]=41
	lst[1]=87
	lst[2]=88
	print(id(lst))

lst=[10,20,30]
print(id(lst))
ls(lst)
print(lst)'''

'''def add(m,*n):

	k=m
	for i in n:
		k+=i

	print(k)

#variable length fun.
add(120,104,5002,360)'''

'''def details(**n):
	for i,j in n.items():
		print(i,j)



details(name='jak',age=22,city='chennai')'''#keyword variable length fun.

'''g=50#global variable
print("id of global g", id(g))
def some():
	
	tt=globals()['g']
	print(id(tt))
	g=500
	print(g)#printing local one cz the fn. will gve preference to the to local variables
	globals()["g"]=5000#by this way we can modifiy and access the global variales inside the fn. itself

some()
print(g)'''#printing global one

###########################odd & even no. using lst

def fun(ls):
	ev=0
	od=0

	for i in ls:
		if (i%2)==0:
			ev+=1
		else:
			od+=1

	return (ev,od)

ls=[58,98,51,79,63,44,88,63,52,100,1004,117,713,413]
even,odd=fun(ls)

#print('even_count=',even,'odd_count=',odd)
print('EVEN : {} ODD: {}'.format(even,odd))#using string fn. and printing
