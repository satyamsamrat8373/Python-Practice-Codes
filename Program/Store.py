'''
# Sample input:
'Milk: 2.50'
'Egg: 2.50'
done

#Sample Output:
'Milk: 2.5'
'Egg: 2.5'

'''

product = {}
while True:
    user = input().strip()
    if user == "done":
        break
    name, price = user.split(",")
    name = name.strip()
    price = float(price.strip())
    product[name] = price

for pname,pprice in product.items():
    print(f"{pname}: {pprice}")

