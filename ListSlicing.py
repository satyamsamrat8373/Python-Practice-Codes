#list_name[start:end-1:steps]
# Here steps means how much we steps to add
li1 = [10,20,30,40,50,60]
sub_list = li1[0:4:1]
print(sub_list) # [10, 20, 30, 40]

sub_list2 = li1[1::]
print(sub_list2) # [20, 30, 40, 50, 60]

sub_list3 = li1[::2]
print(sub_list3) # [10, 30, 50]

# For reversing the list.
reverse_li1 = li1[::-1]
print(reverse_li1)

# For fetching last element only.
print(li1[-1::]) # 60 will be output


# Q. What is list slicing?
# => It is used to create sublist from main list.
# Syntax: list_name [start:end - 1:steps]

