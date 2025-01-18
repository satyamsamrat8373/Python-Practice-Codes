'''
1. In Tuples we can store Homogeneous as well as Heterogeneous Data.
2. In tuples we can store Duplicates.
3. Tuples are ordered collection of data.
4. Tuples are Immutable: Once we declare the tuple we cannot modify it.

'''

tup1 = (10,22,5.55,'Kodnest',True,10)
# print(tup1)

# We cannot change,remove or add in tuples it is Immutable.
# tup1.append("Satyam")
# print(tup1) // error

# we can fetch by name:
# print(tup1[2])

# Deletes the tuples:
del tup1
# print(tup1) #error

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)

#Tuple with singleton we give one comma after one variable.
tup = (10, )
print(tup, type(tup))

new_tup = (10,20,30,40)
#ele1 = new_tup[0]
#ele2 = new_tup[1]

# UnPacking of tuple
ele1,ele2,ele3,ele4 = new_tup
print('value of ele1', ele1)