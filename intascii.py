# take ascii value from user and print character from its ascii value
lst = input().split()
for i in range (len(lst)):
    lst[i] = int(lst[i])
    print(chr(lst[i]))
