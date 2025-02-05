class Demo1:
    def __init__(self,name):
        self._name = name #protected variable as name
    def disp1(self):
        print(self._name)
d1 = Demo1("Satyam")
print(d1._name)
d1.disp1()

class Demo2(Demo1):
    def disp2(self):
        print(self._name)
d2 = Demo2("Samrat")
print(d2._name)
d2.disp2()

class Demo3:
    def disp3(self):
        print(d1._name)
d3 = Demo3()
d3.disp3()

'''
    The variables which are protected can be accessed
    inside the same class, outside the class
    inside the child class and inside non-child class.

    The variables which are protected should be accessed
    inside the same class and inside the child class and
    this is the programmers duty to follow these rules.
'''