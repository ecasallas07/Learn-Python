# inheritance elements

class Person:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        

# Herencia
class Student(Person):
    def __init__(self,name,lastname):
        #hacen lo mismo, super, llama la clase principal, solo que con super no se pone self
        Person.__init__(self,name,lastname)
        super().__init__(name,lastname)
                    

class StudentUniversity(Person):
    def __init__(self,name,lastname,year):
        super().__init__(name,lastname)
        self.year_graduation = year
    def welcome(self):
        print(f"Welcome to University {self.name} {self.lastname}, at {self.year_graduation} year")
            


object1=StudentUniversity('Esteban','Casallas',2021)                
print(object1.welcome())