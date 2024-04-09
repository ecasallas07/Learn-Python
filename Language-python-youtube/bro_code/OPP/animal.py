class Animal:
    alive= True

    def eat(self):
        print("This animal is aeting")
    

    def sleep(self):
        print("This animal is sleeping")

# inheritance 
class Rabbit(Animal):        
    
    def run(self):
        print("This rabbit is running")
class Fish(Animal):

    def swim(self):
        print("this fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hwak is flying")



rabbit = Rabbit()    
fish - Fish()
hawk = Hawk()

#method inheritance
print(rabbit.eat())
print(fish.sleep())

#mehtos owner of each class
print(rabbit.run())
print(fish.swim())
print(hawk.fly())
