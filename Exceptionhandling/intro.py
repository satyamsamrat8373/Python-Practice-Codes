# def disp():

#     a = 10
#     b = 0
#     print(a/ b) # ZeroDivisionError

# disp()

def disp2(a,b):
    try:
        print(a / b)
    except:
        print("Some error handled")

disp2(10,0)
disp2(5,2)
disp2(12,16)