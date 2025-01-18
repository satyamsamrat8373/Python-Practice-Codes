# 1st way of Accepting the user input in list.
# li =[]
# num = int(input("Enter count of elements: "))
# for i in range(num):
#     ele = int(input(f'Enter Element at index {i} : '))
#     li.append(ele)

# print(li)

# Output: 
'''
        Enter count of elements: 4
        Enter Element at index 0 : 1
        Enter Element at index 1 : 2
        Enter Element at index 2 : 3
        Enter Element at index 3 : 4
        [1, 2, 3, 4]
'''

# 2nd Way for user input in list.

#input2 = input("Enter space separated elements: ")
#print(input2, type(input2)) # 10 20 <class 'str'>
#res = input2.split()
#print(res)  # ['12', '20', '12']

# If we want to convert it in integer.

#res = list(map(int,res))
#print(res)



tup = tuple(map(int,input("Enter space separated element: ").split()))
# print(tup)

li1 = list(map(int,input().split()))
print([i for i in li1 if i % 2== 0])