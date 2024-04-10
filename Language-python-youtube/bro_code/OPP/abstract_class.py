# abstract class =  a class wich contains one or more abstract methods
# abstract method =  a method that  has a declaration  but does  not have  an implementation
from abc import ABC, abstractmethod


class Vehicule(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod    
    def stop(self):
        pass



class Car(Vehicule):
    def go(self):
        print("You drive the car")

