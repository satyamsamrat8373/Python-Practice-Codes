# Function Declaration:

# 1. Without Input and Without return type.
def add():
    a = 10
    b = 20
    res = a + b
    print(res)
add()

#2. With input and Without return type
def sub(a,b):
    print("Sub of 2 num: ", a - b)
sub(11,3)

#3. Without Input and With return type.
def mul():
    a = 2
    b = 3
    return a * b
res =mul()
print(res)

#4. With input and with return type.
def div(a,b):
    return a / b
print(div(11,2))