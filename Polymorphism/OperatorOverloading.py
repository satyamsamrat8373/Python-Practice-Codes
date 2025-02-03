class Demo1:
    def disp1(self):
        print('Inside disp1')
    def __str__(self):
        return 'Hello world!'
    def __sub__(self, other):
        self.a = 20
        other.b = 30
        return self.a - other.b


class Demo2:
    def disp2(self):
        print("Inside disp2")
    def __str__(self):  #Dunder method
        return 'Hello'

d1 = Demo1()
d2 = Demo2()

# In Python If we print reference variable then it will display string representation of an address of an object.

# In the above example we have overriden the __str__ methods in their respective classes.
print(d1) 
print(d2)
print(d1 - d2)
'''
    Dunder Method: The methods which has suffix and prefix of __. These dunder methods can be called as magic methods 
    because as programmer we no need to call any methods, automatically methods will be invoked.
'''