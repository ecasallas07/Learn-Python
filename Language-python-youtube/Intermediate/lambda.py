import reduce

# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(1, 2, 3))


square = lambda x: x**2
print(square(10))


# decorators functions

def gretting():
    return 'Weolcome python'

def uppercase_decorator(function):
    def wrapper():
        func =function()
        make_upercase = func.upper()
        return make_upercase
    return wrapper


# one form
g=uppercase_decorator(gretting)
print(g)

# two form
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())  
    
    

# syntax map(function, iterable)    
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']


def upper_function(word):
    wl = word.upper()
    return wl
     
revision_users =  map(upper_function,names)
print(list(revision_users))   # save in the list, beacuse the map iterable in the function


# siyntax filter(function,iterable)
# this function is used o filter response boolenas between true or false
numbers = [1, 2, 3, 4, 5]  

def odd(num):
    if num%2==0:
        return True
    return False

filter_numbers_par = filter(odd, numbers)
print(list(filter_numbers_par))


# reduce function
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)   