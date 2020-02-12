'''class grp:
    a=0
    def __init__(self,a,b):
        self.Name=a
        self.Reg=b

    def fn(self):
        print("NAME: ",self.Name,"\t\t", "REG: ",self.Reg)


obj_1=grp("JAK",10)
obj_2=grp("RAAM",25)

obj_2.a=150
print(obj_2.a)
obj_1.fn()
obj_2.fn()'''

class a:
    def __init__(self):
        self.name
        self.data

    def dis(self):
        print("NAME:",self.name,"DATA:",self.data)

    def compare(self,other):
        if self.data==other.data:
            return True
        else:
            return False


student_1=a()
student_2=a()

student_1.name="JAK"
student_1.data=(int)(500)

student_2.name="Joo"
student_2.data=(int)(500)

if student_1.compare(student_2):
    print("same")
else:
    print("not")

student_1.dis()
student_2.dis()
