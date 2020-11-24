score = [10, 20, 30, 56, 80, 43]
print(score)

print(score[0])
print(score[4])
print(score[-4])
print(score[-5])

print(score[:]) # new/ shallow copy of list #

print(score + [1,2,3,])
print(score + ["A","B","c"])

number = [1,2,3,4,5,6]
number[2]=90
print(number)

# append:

number.append(100)
print(number)

number.append(7**3)
print(number)

# nesting list:

a = ['a','b','c','d']
k = [10,20,30,40]
j = [a,k]
print(j)
print(x[0])
print(x[1])

print(x[0][1])
print(x[1][2])
