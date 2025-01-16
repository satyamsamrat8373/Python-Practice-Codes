'''
1. In Set we can store homogeneous as well as Heterogeneous data.
2. Order of Insertion is not same in Set.
3. Duplicates are not allowed in Set.
4. Set does not support indexing of data.
'''

s1 = {10,True,'kodnest',10,20,55.44}
print(s1)

# add(): Used to add element in the set.
s1.add(500)
print(s1)    # {True, 20, 500, 55.44, 10, 'kodnest'}

# remove(): It will remove the specific element
s1.remove(55.44)
print(s1)

#Pop(): Without index will delete and return one element.
poped_ele = s1.pop()
print(poped_ele)  # True
print(s1)   # {20, 500, 10, 'kodnest'}