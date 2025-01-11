'''
    For control_variable in iterable_object
'''
for i in 'Kodnest':
    print(i,end ="")
for j in [10,20,30]:
    print(j + 5)

for num in range(1,11,2):
    print(num)

#WAP to print all even numbers from 1 to 10
for i in range(2,11,2):
    print(i,end = " ")

i = 0
while (i < 10):
    print(i + 100)
    i = i+1

for i in range(1,11):
    if (i == 6):
        continue
    else:
        print(i)

for i in range(1,11):
    if (i == 5):
        break
    else:
        print(i,end =" ")
