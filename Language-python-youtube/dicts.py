## dictionarys

my_dict  = {}
my_other_dict = dict()


print(type(my_dict))

my_other_dict = {"Nombre":"Esteban","Apellido":"Casallas","Edad":17}

my_dict= {
    "Nombre": "Juan",
    "Empresa": "Vass Latam",
    "Edad": 18,
    "Calle": "Soacha"
}

print(my_dict)

my_dict["Nombre"] = "David"
print(my_dict["Nombre"])


del my_dict["Calle"]
print(my_dict)

print("Esteban" in my_dict) # true or false

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
# print(my_dict.fromKeys(("Nombre",1)))


