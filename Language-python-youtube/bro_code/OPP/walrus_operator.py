# Walrus operator

# new to python 3.8 version 
foods = list()
while True:
    food = input('what food do you like?: ')
    if food == 'quit':
        break
    foods.append(food)

#  the same code before with walrus operator
foods = list() 
while food:= input('what food do you like?: ') != 'quit':
    foods.append(food)
    
    