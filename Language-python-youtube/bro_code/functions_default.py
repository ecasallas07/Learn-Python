# imports functions
import functools


#map = applies a function to each item in an iterable (list,tuple,etc)
# map(function,iterable)


store = [
    ("shirt",20.00),
    ("pants",40.00),
    ("shoes",24.00),
    ("socks",19.00)
]

# to_euros = lambda data: (data[0],data[1]*0.82)
# to_dollars = lambda data: (data[0],data[1]/0.82)

# store_dollars = list(map(to_euros,store))

# Example to map functions
letters = ('esteban','daniel','casallas','hernandez')
def counter(text):
    return len(text)

x = list(map(counter,letters))
print(x)
# convert a list variable of map, when is tis variable is equal to map(counter,letters) without list()
print(list(x))

# Filter function

friends= [
    ("Esteban",20),
    ("Daniel",40),
    ("Casallas",13),
    ("Hernandez",15)
]

age = lambda data: data[1] >= 18

#search for >= 18 years
drinking = list(filter(age,friends))
print(drinking)


# reduce function = apply a function to an iterable  adn reduce it to a single cumulative value
letters = ["H","E","L","L","O"]

word = functools.reduce(lambda x,y:x+y,letters)
print(word) 





