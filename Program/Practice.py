# Find the second lowest in the list.

li = list(map(int,input().split(",")))
li = list(set(li))
# li = li.sort() --> Sort method won't return anything.
li.sort()

# Largest:
print("The largest in the list is:", li[-1])

#Second_Largest
print("The Second largest in the list is:", li[-2])

#Second lowest
print("The Second lowest in the list is: ", li[1])

#Lowest
print(f"The lowest in the list is: {li[0]}")

