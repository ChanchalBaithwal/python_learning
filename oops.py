#22nd July
class webseries:
    def __init__(self, name, season, eposide):
       self.name = name
       self.season = season
       self.eposide = eposide
       print('i am hit')

    def say_my_name(self):
        return self.name

web_1 = webseries('game of thrones',1, 1)
web_2 = webseries('hatim', 1, 2)
print(web_1.name, web_2.name)



class vehicle:
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
    print('hiiiiiiiii')



#vehicle properties using class
class vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def get_brand(self):
        return f'this brand is {self.brand}'


class Car(vehicle):
    def __init__(self, brand, color, type_):
        super().__init__(brand, color)
        self.type_ = type_
        self.brand = brand
    
    def get_color(self):
        return f'this color is {self.color}'
    
    def get_type(self):
        return f'this type is {self.type_}'
    
sedan = Car('Toyota', 'Red', 'Sedan')
print(sedan.get_brand())
print(sedan.get_color())
print(sedan.get_type())


#school information using class
class school:
    def __init__(self, name):
        self.name = name
        
    
    def get_name(self):
        return f'this name is {self.name}'


class Student(school):
    def __init__(self, name, std, roll_no):
        super().__init__(name)
        self.std = std
        self.roll_no = roll_no
    
    def get_name(self):
        return f'this name is {self.name}'
    
    def get_std(self):
        return f'this std is {self.std}'

    def get_roll_no(self):
        return f'this roll_no is {self.roll_no}'
    
Div= Student('Chanchal', 'iv', '5' )
print(Div.get_name())
print(Div.get_std())
print(Div.get_roll_no())

class Teacher(school):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    
    def get_name(self):
        return f'this name is {self.name}'
    
    def get_salary(self):
        return f'this salary is {self.salary}'
    
Div= Teacher('Priya', '4000')
print(Div.get_name())
print(Div.get_salary())






