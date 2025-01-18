# map(function, iterable_Object) ---> Iterator Object

def double(x):
    return x * 2

l1 = [1,2,3,4]
double_li = list(map(double,l1))
print(double_li)

tup = ('10','20','30')
print(tup) # ('10', '20', '30')
tup = tuple(map(int,tup))
print(tup) # (10, 20, 30)

# Convert each integer into float.
li2 = [1,5,66]
li2 = tuple(map(float,li2))
print(li2) # (1.0, 5.0, 66.0)