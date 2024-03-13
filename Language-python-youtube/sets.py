### set ###
# definition in spanish: COLECCION DESORDENADA  DE VALORES UNICOS, ELIMINA VALORES UNICOS

my_set = set()
my_other_set = {}

print(type(my_other_set)) # dictionary

# function for uses in the set
my_other_set = {1,'c'} # un set no admite repetidos elementos

my_other_set.add('santo') 
print(my_other_set) # set es desrodenado, por ello no se puede acceder a sus elementos en index o nombre, porque se ordenan aleatoriamente

print("santo" in my_other_set) # valid if exist this element

my_other_set.clear()

my_set = {1,2,3,4,5,6,7,8,}
my_other_set = {'a', 'b', 'c', 'd'}
my_new_set = my_set.union(my_other_set)

print('\n================================')
print(my_new_set)

#elements diferentes
print(my_new_set.difference(my_other_set))