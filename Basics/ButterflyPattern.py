#Butterfly Pattern
row = int(input())
for i in range(1,row + 1):
    print("*" * i, end ="")
    print(" " * (2 * (row - i)),end="")
    print("*" * i)
for i in range(row - 1, 0, -1):
    print("*" * i, end="")
    print(" " * (2 * (row - i)), end="")
    print("*" * i)


 