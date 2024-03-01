### strings  ###

my_string = 'hello'
my_name = 'esteban'


print(len(my_string))
print(len(my_name))


sentence = my_string +  " " + my_name

# linea break \n

my_line_new_string = "Hello my people\n I have 17 years old"
print(my_line_new_string)


# tabulate space
my_tab_string = "\tGreat mommetn for play soccer"


# formating

name, surname, age = "Esteban" ,"Casallas", 17
# one form
print( "My name is {} and my surname is {} and my age is {} ".format(name,surname,age)) # this best form for concatention
print( "My name is %s and my surname is %s and my age is %d "%(name,surname,age))
print(f"My name is {name} and my surname is {surname} and my age is{age}")

# division of elements
language = "python" 
language_slice = language[2:4]
reversed_language  = language[::-1]

# function of strings

print(language.capitalize()) # first letter of language
print(language.upper())
print(language.count('t')) # how much letter in word
print(language.isnumeric()) # false
print("1".isnumeric()) # true


