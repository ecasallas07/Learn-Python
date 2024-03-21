## loops

#while

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
    

# for    
     
my_list = [1,2,3,4,5]    

for element in my_list:
    print(element)


my_dict = {"Nombre":"Esteban","age":12}
for value in my_dict.values():
    print(value)
    if value == 12:
        break
    else:
        continue
    
    
# the  range function
lst = list(range(11))
print(lst)


# iterator list

list_example =['a','b','c','d','e','f','g','h','i']

# for in string elements
for i  in range(len(list_example)):
    print(list_example[i])


# iterateor for elements dictionary  
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)
    

for key,value in person.items():
    print(f"{key} : {value}")    
    
    



#exercise 01    
elements ='########'    
for i  in range(len(elements)):
    print(elements[:i])
    
# exercise 02

cadena_string = '########'    
for i in range(len(cadena_string)):
    print(" ".join(cadena_string))
    
# exercise 03
for i in range(11):
    print(f"{i} x {i}: {i*i}")    


#exercise 04 --> Use for loop to iterate from 0 to 100 and print the sum of all numbers.

el = 0
for i in range(101):
    sum_i = i + el
    el = sum_i
print(f"the result of the all numbers is: {el}")        