#function syntax
#print hello function using function
def greet():
    print("hello world!")
greet()


def greet():
    print("hello world!")
    return 'hi mars!'
greet()
print(var)      #return statement will print here


#factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
fact_of_5 = factorial(5)
fact_of_10 = factorial(10)
print(fact_of_5)
print(fact_of_10)



#print a table of any number
def table(n):
    for i in range(1, 11):
        tab = n*i
        print(tab)
num = int(input('enter a number'))
table(num)


#return list 
def return_list():
    return [1, 2, 3]
print(return_list())


#function to print true or false if a case is upper or lower respectively
def string(st):
    if st == st.upper():
        return True
    else:
        return False
inp = input('enter a string:')
print(string(inp))



#print sum of ascii value of a string
st = input('enter a string:')
def sum_of_ascii(st):
    sum_ = 0
    for i in st:
        sum_ = sum_ + ord(i)
    return sum_
print(sum_of_ascii(st))


#method 2 (using map)
def sum_of_ascii(input_string):
    return sum(map(ord, input_string))
inp = input('enter a string:')
print(sum_of_ascii(inp))



#take username and pswrd and print a string contaning 1st 4 letters of username and last 4 from password
def user_pass(username, password):
    return(username[0:4] + password[-4:])
name = input('enter username:')
password = input('enter password:')
print(user_pass(name, password))


#return a no. which represent that immediate character comes in the string is same as alphabets sequence
inp = input('enter a string:')
def imm_char(inp):
    count = 0
    for i in range(0,len(inp)-1):
        if ord(inp[i]) + 1 == ord(inp[i+1]):
            count += 1
    return count
print(imm_char(inp))



# take list into input and print elements which are even

lst_ = [1, 2, 3, 4, 5, 6, 6, 8, 9]
def even_lst(lst_):
    for i in lst_:
        if i % 2 == 0:
            print(i)
        
even_lst(lst_)
    

   