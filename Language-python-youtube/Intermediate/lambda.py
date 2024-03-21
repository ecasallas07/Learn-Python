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
    