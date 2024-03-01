# single line coment
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

phrase = "Hello, World!"
print(phrase)

# Multiline string

text = """
    I am learning englhis every day
"""
print(text)


#### Unpacking characters 

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n


# comment lines
"""
    Comments for word
"""

# accesing a characters

language = "Python"
print(language[0])
last_index = len(language) -1 

# Challengue capitalize 
# Convert first lette to Capital letter
challengue = "when are you"
print(challengue.capitalize())  # When are you

# endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False


# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'


challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# format()	formats string into nicer output    
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.


# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'


# replace(): Replaces substring inside
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'


# split():Splits String from Left
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']


