class A:

    def __init__(self):
        self.n=1

    def __iter__(self):
        return self

    def __next__(self):

        if self.n<=10:
            v=self.n
            self.n += 1

            return v
        else:
            raise StopIteration



a=A()

print(next(a))

for i in a:
    print(i)

'''num=list(range(1,10+1))
n=iter(num)
print(next(n))
for i in num:
    print(next(n))'''
