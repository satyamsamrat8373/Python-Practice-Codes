'''
    Three types of control constructs:
    1.Conditional: if,else
    2.Loop: while,for
    3.Jumping: break,continue,pass
'''
def age(a):
    if (a>18):
        print("You can vote")
    else:
        print("You can't vote")
age(22)


def checkage(age):
    if (age<18):
        print("Child")
    elif(age > 18 and age < 65):
         print("Adult")
    else:  
        print("Senior Citizen")
checkage(int(input("Enter the age:")))