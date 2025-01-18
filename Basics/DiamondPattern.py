row = int(input())
for i in range(1, row + 1):
    print(" " * (row - i),end = "")
    if i == 1:
        print("*")
    else:
        print("*" + "*" *(2 * i - 3) + "*")
for i in range(row -1, 0, -1):
    print(" " * (row - i), end ="")
    if i == 1:
        print("*")
    else:
        print("*" + "*" * (2 * i - 3) + "*")