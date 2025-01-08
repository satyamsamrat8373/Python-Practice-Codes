# Strings are Immutable : 
""" 1. Once we declare the Strings we cannot modify it, 
       if we try to modify the string it will create new String.

    2. If new String does not have any reference variable then it will be removed.

    3. Python Internally uses String Interning.

    4. String Interning is the process of Checking string intern pool
       before creating any new object.

    5. Whenever we want to create new object, Python First will check string
       intern pool, whether that object already exist or not.

    6. When Object already exist in the string intern Records then
       address of existing object will be reused.
"""

s1 = "kodnest"
s1 = s1.upper()
print(s1)
s1 = "ddf"
print(s1)

# id is used to give reference address of that variable.
s2 = 'K'
print(s2, id(s2))

s3 = "Hello"
s4 = "World"
print(s3, id(s3))
print(s4, id(s4))

# Fetching first and last character of String
print(s3[0]) #H
print(s3[-1]) #o

# Fetching Address of one Individual Character
print('Id of H: ', id(s3[0]))
print('Id of W: ',id(s4[0]))


print('ID of O of s4: ',id(s4[1]))