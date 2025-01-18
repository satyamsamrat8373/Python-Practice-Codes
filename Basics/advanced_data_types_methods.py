# List Method
li1 = list('kod')
print(li1) #['K', 'o', 'd']

li2 = list((10,20))
print(li2)

li3 = list({100,200})
print(li3)

li4 = list({"Name": "Satyam", 'age': 22})
print(li4)

li5 = list(range(1,11))
print(li5)

# Tuple Method (iterable_object)
tup1 = tuple([10,20,30])
print(tup1)
tup2 = tuple({100,200})
print(tup2)
tup3 = tuple(range(1,11))
print(tup3)
tup4 = tuple('kodnest')
print(tup4)
tup5 = tuple({'name': "Satyam",'age':22})
print(tup5)


# set(iterable Object):
s1 = set([10,20,20,30])
print(s1)

# dict(iterable_object:key:value)
d1 = dict([['name',"satyam"],['age',23]])
print(d1)
