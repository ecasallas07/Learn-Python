# higher Order functions

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)
    
    
# function execute overload funcion     
hello(loud)
hello(quiet)    

