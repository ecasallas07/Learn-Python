class Car:

# constructor class, automaticate initiallation
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year 
        self.color = color 
   #--------------------------------------------     
   # methods of the classs 
    def drive(self):
        print(f"This {self.model}  is driving")
    
    def stop(self):
        print(f"This {self.model} stop")
