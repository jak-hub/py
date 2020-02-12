def fib(a):
	z=0
	p=[]
	for i in range(0,a+1):
		if (i==0):
			x=0
			p.append(x)

		elif (i==1):
			x=1
			p.append(x)

		else:
			x+=p[z]
			p.append(x)
			z+=1
					
	print(p)	
	return x



print(fib(10))
