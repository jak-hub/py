from time import *
from threading import *

class A(Thread):
    def run(self):
        for i in range(5):
            print("HELLO")
            sleep(0.5)


class B(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(0.5)

t1=A()
t2=B()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")