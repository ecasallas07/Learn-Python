# Exeption Handling

number_one = 10
number_two = "5"

# try except
try:
    pass
except:
    pass    


# try except else
try:
    print(number_one + number_two)
except:
    print("Error handling for operation")    
else:
    print("the executed contiue")    
    
    
# try except else finally
try:
    print(number_one + number_two)
except:
    print("Error handling for operation")    
else:
    # se ejecuta solo cuando la excepion no se ejecuta
    print("the executed contiue")
finally:
    # siempre se jecuta sin importar si ingresa o no a la exepcion
    print("the executed contiue")            
    
# Exception for  typw

try:
    print(number_one + number_two)
except ValueError:
    print("The error of value")        
except TypeError:
    print("the error of type")


# Catch Exceptio error

try:
    print(number_one + number_two)
except ValueError as error:
    print(error.message)
except TypeError as my_ramdom_error:                
    print(my_ramdom_error)