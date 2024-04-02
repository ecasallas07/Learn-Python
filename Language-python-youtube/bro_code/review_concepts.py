import random

# Tuples : collection which is ordered and unchengeable
student = ("Esteban",20,"Casallas")
print(student.count())
student.index("Esteban")


# Sets: collection which is undered and indexed, No duplicate values 
utentsils = {"Esteban","Deisy","Gutsavo"}
dishes = {"Casallas","Hernandez","Saaavedra"}
utentsils.add("Daniel")
utentsils.remove("Esteban")
utentsils.cler()
utentsils.update(dishes)

 # Dictionarys
  # A changeable, unordered collection of unique key:value pairs
cars = {'mercedez':'clase-g-30', 'renault':'sandero','chevrolet':'optra'}
cars['mercedez']
cars.get('sandero')
cars.keys()
cars.values()
cars.items()
cars.pop('renault')


# *args = parameter that will pack all argument into a tuple useful so thta a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum+= i
    return sum
print(add(1,2,3,4))

# random
x = random.randint(1,6)
y = random.random()
myList = ['rock','paper','scissors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K"]
random.shuffle(cards)
print(cards)

# Exception
