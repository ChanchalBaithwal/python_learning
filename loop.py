lst = [1,2,3,4,5,6,7,8,4,10]
fname = 'chanchal'
for i in [1,2,3]:
    for j in['a','b','c']:
        print(i,j)

#using range
two_table = range(2, 21, 2)
print(list(two_table))

for i in range(1,10):
    print(i)

for i in range(len(lst)):
    print(lst[i])
print('  ')

for i in range(0, len(lst), 2):
    print(lst[i])

#nested
for i in [1, 2, 3]:
    for j in ['a', 'b', 'c']:
        print(i,j)

#while
i = 0
while i < 5:
    print(i)
    i += 1
