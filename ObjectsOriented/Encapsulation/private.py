class Demo1:
    def __init__(self,name):
        self.__name = name # Private variable as name.

    def getName(self):
        return self.__name
    
    def setName(self,newName):
        self.__name = newName

d1 = Demo1("Akash")
# print(d1.name) # error
print(d1.getName())

d1.setName("Satyam")

print(d1.getName())