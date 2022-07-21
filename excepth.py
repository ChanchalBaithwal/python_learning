#integer number divide by 0
try:
    print(5/0)
except ZeroDivisionError:
    print('you can not divide it by 0')


#integer number divide by a character 
try:
    print(5/'a')
except TypeError:
    print('you can not divide it by a')


