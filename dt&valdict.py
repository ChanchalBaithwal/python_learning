no_of_elem = int(input('enter a number'))
map_ {
    'str' : [],
    'int': [],
    'float': []
}
for i in range(no_of_elem):
    dt = input('enter datatype')
    val = input('enter value of above datatype')
    if dt == 'str':
        map_['str'].append(val)
    elif dt == 'int':
        map_['int'].append(val)
    elif dt == 'float':
        map_['float'].append(val)
    else:
        print('please initialize a empty list for (dt)', format(dt))
    print(map_)

