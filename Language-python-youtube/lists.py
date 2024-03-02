### lists ###

# forms of declareted lists
my_list = list()
my_other_list = []


my_list = [1,2,3,4,5,6,7,8,9,10]

print(my_list, len(my_list))

my_other_list = [1,3,4,"Esteban","Senior",3,3,3,3]

print(my_other_list, len(my_other_list), type(my_other_list))
print(my_other_list.count(3)) # cuenta las aveces que el elemento dentro de count en este caso 3 esta en la lista my_other_lists

# add elements a my lists
my_other_list.append("VASS LATAM")
print(my_other_list)


my_other_list.insert(1,"PAR SERVICIOS") #insert element in the position 1 od the lists
print(my_other_list)

my_other_list.remove("Esteban") # name of value exactly for delete elements
print(my_other_list)


print("\n********************************")
print(my_list)
my_list.pop() #remove the end element
print(my_list)

my_list.pop(2) #element delete for the index 2 
elements = my_list.pop(1)  # delete the element lisrts, but i can save in a variable


# delete element lists
del my_list[2]
print(my_list)

my_list.clear()
print(my_list)




my_new_list = ["A", "B", "C"]
my_new_list2 = my_new_list.copy()

print(my_new_list)
print(my_new_list2)


