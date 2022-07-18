# take operation and two integer value from user and print in a list when user enter the details the output must bhi the answer of entered operation.
s = 'shivank is backend developer'
print(s.split())

inp = int(input('enter the number'))
for i in range(inp):
    op, num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    if op =='add':
        print(num1 + num2)
    elif op == 'sub':
        print(num1 - num2)
    elif op == 'mul':
        print(num1 * num2)
    elif op == 'div':
        print(num1 / num2)
    else:
        print('nothing')
    

#take operation and two integer value from user and print in a list when user enter the details the output must bhi the answer of entered operation.    
n = input('how many test cases:')
n = int(n)
for i in range(n):
    op = input('please enter the operation string:')
    op_list = op.split()
    print(op_list)
    if op_list[0] == 'add':
        num1 = int(op_list[1])
        num2 = int(op_list[2])
        print(num1 + num2)
    elif op_list[0] == 'sub':
        num1 = int(op_list[1])
        num2 = int(op_list[2])
        print(num1 - num2)
    elif op_list[0] == 'mul':
        num1 = int(op_list[1])
        num2 = int(op_list[2])
        print(num1 * num2)
    elif op_list[0] == 'div':
        num1 = int(op_list[1])
        num2 = int(op_list[2])
        print(num1 / num2)
    else:
        print('no found')


#take operation and n integer numbers from user and print in a list and when user enter the details the output must bhi the answer of entered operation.
n = input('how many test cases:')
n = int(n)
for i in range(n):
    op = input('please enter the operation string:')
    op_lst = op.split()
    print(op_lst)

    if op_lst[0] == 'add':
        total = 0
        for num in op_lst[1:]:
            total = total + int(num)
        print(total)

    elif op_lst[0] == 'mul':
        for num in op_lst[1:]:
            mult = mult * int(num)
        print(mult)
    else:
        print('no found')
