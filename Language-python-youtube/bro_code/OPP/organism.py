# multi-level inheritance = when a derived (child) class inherits another derived (child)

class Organism:


    alive = True


class Animal(Organism):

    def eat(self):
        print("This animal is eating")



class Dog(Animal):


    def bark(self):
        print("This dog is barking")

object = Dog()        
print(object.alive)
print(object.eat())
print(object.bark())
