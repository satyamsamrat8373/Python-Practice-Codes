'''
# Sample Input 
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

# Sample Output
56.00
'''


d = {}
n = int(input())
for i in range(n):
    name, *score = input().split()
    score = list(map(float,score))
    d[name] = score
tname = input()
for name,score in d.items():
    if name == tname:
        avg = sum(score) / len(score)
print(f"{avg:.2f}")