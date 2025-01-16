li1 = [1,2,3,4,5]
# 1st way for squaring the num

# sq_li =[]
# for i in li1:
#     sq_li.append(i ** 2)
# print(sq_li)

# 2nd way for squaring the num
# [expression,range,condition]
# When we have only if part then write it after for loop.
duplicate_out = [i for i in li1]
#print(duplicate_out)

even = [i for i in li1 if i %2==0]
#print(even)

sq_list = [i**2 for i in li1]
#print(sq_list)

new_li1 = [ele+2 for ele in li1]
#print(new_li1)

# When we have if-else both write it before for loop

even_odd = ['even' if i % 2==0 else 'ODD' for i in li1]
#print(even_odd)

# Questn hackerrank
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

lst = []

lst=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]

print(lst)