class Demo1:
    def __init__(self,name):
        self.__name = name # Private variable as name.

    

d1 = Demo1("Akash")
# print(d1.__name)  #error
print(d1._Demo1__name)

'''
    (1.)NameMangling is the process of providing
    new Name to the private variables.

    (2.)These new names will be provided automatically
    by python for all private members.

    (3.)New name will be provided in the format:
    objectname._className__variableName

'''