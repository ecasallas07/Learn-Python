
# function in [python]

#define function
def first():
    print("My first function in python, awesome!!")
    
    
#call function 
first()    


#definition function

def alert():
    for i in range(3):
        print("Revision of account, Problem of security")
        
alert()


def list_string():
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]        
    
    for i in  username_list:
        print(i)


# function with parameters and arguments 

def hello(name):
    print("Welcome to Python City ", name)        

hello("Esteban")    


# retrun in fucntions

def calculator(sing, num1,num2):

    match sing:
        case "+" :
            result = num1 + num2
        case "-":
            if num1 > num2:
                result = num1 - num2    
            else:
                result = num2 - num1    
        case "/":
            result =  num1 / num2
        case "*":
            result = num1 * num2            
        case _:
            result = "Nothing stupid man"    
    return result        


#function of PYTHON
# __________________________________________________________

print()
type() # return data type of ist input 
max()
min()
sorted() # sorts of components of a list --> organization of from a to z in a list or in form ASC




failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]
sorted(failed_login_list)
max(failed_login_list)

 
