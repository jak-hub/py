row=int(input("ENTER THE ROW: "))

for i in range(row):
    for k in range(row-i):
        print(" ",end="")
	for j in range(i):
		print("*\t",end="")

	print("\n")