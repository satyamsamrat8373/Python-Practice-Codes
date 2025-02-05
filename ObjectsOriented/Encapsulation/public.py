class Demo1:
    def __init__(self,name):
        self.name = name
    def disp1(self):
        print(self.name)
d1 = Demo1("Satyam")
print(d1.name)
d1.disp1()

class Demo2(Demo1):
    def disp2(self):
        print(self.name)
d2 = Demo2("Samrat")
print(d2.name)
d2.disp2()


'''
    The variables which are public can be accessed
    inside the same class, outside the class
    inside the child class and inside non-child class.
'''