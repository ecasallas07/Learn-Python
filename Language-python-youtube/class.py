## class

# when used (pass)  -> significa que esto no ejecuta nada no hace nada pero si dejamos el codigo sin passs generaria error, por lo
# cual se usa para escribir codigo futuro 

class MyEmpityPerson:
    pass



class Person:
        # construct
        #self is obligatoried
        def __init__(self, name, surname, alias = "Sin alias"):
            self.full_name = f"{name} {surname} {alias}"
            # atributte private is with __
            self.__name = name
            self.__surname = surname
            
        def get_name(self):
            return self.__name    
            
        def walk(self):
            print(f"{self.full_name}")
        

# instance of my object
my_person = Person("Esteban","Casallas")
# print(my_person.name)
# print(f"{my_person.name}  {my_person.surname}")
print(my_person.walk())

# insrtance other object

my_other_person = Person("Daniel","Hernandez","elgenio")
print(my_other_person.walk())

# change the value of tha variable  full_name of tha class
my_other_person.full_name = "He is a great genius person"
print(my_other_person.full_name)

# print(my_other_person.__name) # error because of attribute is private
print(my_other_person.get_name()) # getter