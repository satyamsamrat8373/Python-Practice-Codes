# Printing multiple element and index in the same list.

l1 = [10,20,30]
for idx,ele in enumerate(l1):
    print(f"Element index and element: {idx} {ele}")

# Q. Write the Python Program to print all even index element.
l1 = [11,23,44,56,78,99]
for idx,ele in enumerate(l1,start = 1):
    if idx % 2 == 0:
        print(ele) # 23,56,99