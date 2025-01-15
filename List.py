'''
1. In List we can store Homogeneous as well as Heterogeneous Data.
2. In List we can store Duplicate values.
3. List is an ordered collection of Data: Order of insertion is remain as it is in the output.
4. Lists are Mutable: Once we declare the list we can modify it.

'''
list = [10,20,34,3,True,'satyam',33]
# print(list, type(list))

# append(): Will add element at the end of the list.
list.append(300)
# print(list)

#insert(index,element)
list.insert(4,'Added')
# print(list)

#remove(elementname):
list.remove("Added")
# print(list)

#In and not in Operator
# print(20 in list) # True
# print(30 in list) # False

# Pop: Without Argument It will deleted last element from list and return else list.
list.pop()
# print(list)

# Pop(index): With argument will delete the element at specified Index.
# Function will return the value .
removed_el = list.pop(4)
print(removed_el)
print(list)

# del Keyword:
del list[1]
print(list)