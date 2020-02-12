'''def sq():
    n=1
    i=1
    while i<=10:
        s=n*n
        yield s
        n+=1
        i+=1

u=sq()

for i in u:
    print(i)'''

'''def s():
    yield "hi"
    yield "jo"


d=s()
print(d.__next__())
print(d.__next__())
print(s().__next__())
print(s().__next__())'''

def s():
    yield 10

d=s()
for i in d:
    print(i)