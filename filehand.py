#to open,read and close a txt file
file = open('demo.txt', 'r')
# print(file.read())
data = file.read()
#data1 = file.readlines()
file.close()
print(data)


#write a file
file = open('demo.txt','w')
file.write('hellooooooo')
file.writelines
file.close()



#
file = open('demo.txt', 'r')
def read_file_(file):
    dic = {}
    data_ = file.readlines().split()
    print(data_)
print(file.read())


#print subject and students name using dictionary in a txt file
def read_file_and_return_map(file):
    file = open('demo.txt', 'r')
    data = file.readlines()
    map_ = {}
    """
    ["Maths Shivank\n", "Maths Nootan\n"]
    """
    for elem in data:
        """
        "Maths Shivank\n"
        """
        sub, name = elem.split()
        # lst = sub.split() # ['Maths', 'Shivank']
        if sub in map_:
            map_[sub].add(name)
        else:
            map_[sub] = {name}
    file.close()
    return map_

#make demo.txt file and then form a dictionary using function
def read_file_and_return_map(file):
    file = open('demo.txt', 'r')
    data = file.readlines()
    map_ = {}
    
    for elem in data:
        sub, name = elem.split()
        # lst = sub.split() # ['Maths', 'Shivank']
        if sub in map_:
            map_[sub].add(name)
        else:
            map_[sub] = {name}
    file.close()
    return map_

map_ = read_file_and_return_map('name.txt')
print(map_)


#make demo.txt file and then form a dictionary using function
file = open('one.txt', 'r')
def fun_(file):
    dic = {}
    data = file.readlines()
    for i in data:
        sub, name = i.split()
        if sub in dic:
            dic[sub].add(name)
        else:
            dic[sub] = set()
            dic[sub].add(name)
    print(dic)
fun_(file)

#count the max frequency of a word in a given txt file in dictionary
file = open('me.txt', 'r')
data = file.read().split()
def frequency(file):
    dict = {}
    for i in data:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
frequency(file)


#write the words with their frequescies in a file in dictionary form.
file = open('me.txt', 'r')
data = file.read().split()
def frequency(file):
    dict = {}
    for i in data:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
frequency(file)
data = frequency('me.txt')

file = open('collect.txt','w')


#to print number using lambda
inp = lambda n: [i for i in range(n)]
print(inp(5))


#to print multiple of two till powr 6 using lambda
power = lambda n:[i*2 for i in range(n)]
print(power(6))


#to print only even number in given list using filter
def is_even(n):
   return n%2 == 0
# filter('is_even', [1,2,3,4,5,6,7,8,9,10])
a = filter(is_even,[1,2,3,32,2,3,2,454,34])
a = list(a)
print(a)


#print name and length of a webseries using class 
class webseries:
    show_name = 'Suites'
    show_length = '189998999999999999990999999999'

web_series_obj = webseries()
print(web_series_obj.show_name)
print(web_series_obj.show_length)


#to print webseries's name, season and eposide using class and object
class webseries:
    def __init__(self, name, season, eposide):
       self.name = name
       self.season = season
       self.eposide = eposide
       print('i am hit')

web_1 = webseries('game of thrones',1, 1)
web_2 = webseries('hatim', 1, 2)
print(web_1.name, web_2.name)






