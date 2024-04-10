class Duck:


    def walk():
        print("The duck is walking")
    def talk():
        print("The duck is talking")



class Chicken:

    def walk():
        print("The chicken is walking")
    def talk():
        print("The chicken is talking")



class Person():

    def catch(self,animal):
        animal.walk()
        animal.talk()
        print("You caught the critter")



duck = Duck()
person = Person()

person.catch(duck)
