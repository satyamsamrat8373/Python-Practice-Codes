'''
1. Ordered of insertion is same or ordered.
2. It takes Heterogeneous data.
3. We can't give duplicate key while value can be duplicates.
Latest value will come in if key is duplicate.
'''

d1 = {'name': 'Priya','age': 27,'phone':235456}
# print(d1)

d1['name'] = 'pooja'
# print(d1)

# In dict we can store multiple values:
marks = {'sci': 85,'maths':99}
# print (marks)

# for fetching by keys.
for i in d1.keys():
    print(i)

# for fetching by value
for i in d1.values():
    print(i)

# For fetching by key and value both.
for i in d1.items():
    print(i)