# Q. Occurence of Each number.
list1 = list(map(int,input().split()))
d = {}
for i in list1:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
for num, count in d.items():
    print(f"{num} occurs {count} time(s)")