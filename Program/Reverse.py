# Object.reverse() will reverse the original object.
l1 = [10,20,5,7,43,23]
# print('Before reverse',l1)

l1.reverse()
#  print('After reverse', l1)

#reversed(Object):
l2 = [11,5,8,22]
reversed_l2 = list(reversed(l2))
print(reversed_l2) # [22, 8, 5, 11]

li3 = [1,5,2,9]
new = list(reversed(li3)) #-> Creating new reverse list.
print(new) # -> Reversing originl list