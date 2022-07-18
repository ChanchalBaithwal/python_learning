string = input('enter a string')
for i in string:
    if(ord(i)%2 == 0):
        print('even:' +i)