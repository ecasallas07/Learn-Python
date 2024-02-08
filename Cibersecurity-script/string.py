# function of string
str() # convert  the input object into a tring
new_string = str(123);

len() # return the number of elements  in an object

#concante two strings with +
print("Hello " + "World!")

#Methods

# Upper() convert all string in uppercase letters
name = "Hello"
name.upper()
print("hello".upper())

#lowe() convert all string in lowercase letters

lastname = "Hernandez"
lastname.lower()
print("CASALLAS".lower())


#return for index, in this case is H, because index is zero[0]
"HELLO"[0]

#Extract a slice  from a string
print("HELLO"[1:4]) # outpur : ELL. because index E[1] L[2] L[3]


#Use the string method index 
print("Hello" .index("e")) #ouput : 1

#Error, because the string inmutable
my_string = "HELLO"
my_string[1] = "A"