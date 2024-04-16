# dictionary compressions

# example of dictionary  / dictionary ={key: expression for (key,value) in iterable}


cities_1 = {"New York":32 , "San Francisco":40,"Bogota":10}
# modify the value
cities_2 = {key:((value-32)*(5/9)) for (key,value) in cities_1.items()}

cities_3 ={key: value for (key,value) in cities_1.items() if value == "40"}