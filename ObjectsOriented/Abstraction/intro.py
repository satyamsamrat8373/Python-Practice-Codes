from abc import ABC, abstractmethod
class Demo1(ABC):
    pass
    # @abstractmethod
    # def disp1(self):
    #     print("Inside disp1")

d1 = Demo1()

'''
    RULE:-
    (1) If abstract class have does not have any method then object for that abstract class can be created.


    #Concrete Method:
'''
class Demo2(ABC):
    def disp2(self):
        print("Inside disp2")

d2 = Demo2()
d2.disp2()

'''
    (2) If abstract class have only concrete method then object for that abstract class can be created 
    and concrete methods can be invoked.

'''

class Demo3:
    def info(self):
        print('Inside info')
    @abstractmethod
    def disp3(self):
        print("inside disp3")

class Demo4(Demo3):
    pass
d4 = Demo4()
d4.info()