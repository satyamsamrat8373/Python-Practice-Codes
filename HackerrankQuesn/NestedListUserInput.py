# sub_list_count = int(input())
# for i in range(sub_list_count):


# Sample input
'''
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

#Sample output
Berry
Herry
'''
li = []
n = int(input())
for i in range(n):
    name = input()
    score = float(input())
    li.append([name,score])

scores = []
for name,score in li:
    scores.append(score)
scores = list(set(scores))
scores.sort()

name_li =[]
secondscore = scores[1]
for name,score in li:
    if score == secondscore:
        name_li.append(name)

name_li.sort()
for name in name_li:
    print(name)

