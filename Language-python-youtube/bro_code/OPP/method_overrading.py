 # method overrading
# Overrading methods about 

 
class Animal:
    
    def eat(self):
        print("This animal is eating")
     
class Rabbit(Animal):

    def eat(self): 
        print("This rabbitn is eating") 

rabbit = Rabbit() 
rabbit.eat() 
