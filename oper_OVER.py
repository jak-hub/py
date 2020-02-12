"""class S:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        self.m4= m1
        self.m5= m2
        self.a=m1
        self.b=m2
        self.x = m1
        self.z = m2

    def __add__(self,other):
        a=self.m1+other.m1
        b=self.m2+other.m2

        s3=S(a,b)
        print(a,b)
        return s3
    def __sub__(self,other):
        x=self.m1-other.m1
        z=self.m2-other.m2

        s3=S(x,z)
        '''print(m1,m2)'''
        return s3

s1=S(10,22)
s2=S(55,25)
#s3=s1+s2
s3=s1-s2
print(s3.a,s3.z)"""

class A:
    #p=0
    #q=0
    def __init__(self,a,b):
        self.x=a
        self.y=b
        self.p=a
        self.q=b
    def __add__(self,other):
        p=self.x+other.x
        q=self.y+other.y

        T=A(p,q)
        #print(p,q)
        return T
    def __sub__(self,other):
        p=self.x-other.x
        q=self.y-other.y

        T=A(p,q)
        #print(p,q)
        return T
    def __gt__(self,other):
        #T=A(100,50)
        if self.x<other.x:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.p,self.q)

u=A(10,20)
v=A(50,100)

T=u+v

print(T.p,T.q)

T=u-v

print(T.p,T.q)

T=u<v

print(T)
print(u)