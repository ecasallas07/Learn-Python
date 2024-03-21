# OOP - python
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
# class constructur

# el primer parametro de una funcion en OOP siempre es la referencia de la clase, se puede conocer como sefld, pero se le pude poner cualquier nombre pero simepre
# es el primer parametro

class Person:
    def __init__(self,name):
        self.name=name

p = Person('Esteban')        
print(p.name)
print(p)


class Car:
    def __init__(self,model,year,price):
        self.model = model
        self.year = year
        self.price =  price
    
    #method    
    def person_info(self,user):
        return f'Model of the car: {self.model}, Year of the car: {self.year} and Price: {self.price} for the person {user}'
                

car1 = Car('Chevrolet','1990','10.000.000')       

print(car1.person_info('Esteban'))


class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    # the form return elments of string the funtion __init__    
    def __str__(self):
        return f"{self.name}({self.age})"    