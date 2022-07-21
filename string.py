#given a string in i/p & create a dict with info of freq of chars
string = input('enter a string')
all_freq = {}
for i in string:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print ("Count of all characters is :\n " +  str(all_freq))


# counting of capital letters in small letters
n = input('enter a string')
st = n.casefold()
map_ = {}
for i in st:
    if i in map_:
        map_[i] += 1
    else:
        map_[i] = 1
print(map_)


#break loop
for i in range(5):
    if(i == 3):
        break
    else:
        print(i)



#loop of push & pop in list until user enter stop
inp = int(input('enter the number'))
lst  = [ ]
for i in range(inp):
    op = input().split()
    if op[0] == 'push':
        lst.append(op[1])
        print(lst)
    elif op[0] == 'pop':
        lst.remove(op[1])
        print(lst)
    elif op[0] == 'stop':
        break





            



