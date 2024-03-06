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