# Area

base = int(input("Enter the base of the triangule:   "))
height = int(input("Enter the height of the triangule:   "))

operation = (base * height) / 2

print("The area of the traingule: ", operation)


#-------------------------------------------------
# Radius of circle

# constant
PI = 3.14

radius = int(input("Enter the radius of the circle: "))

# pow : function for operation of exponents
area = PI * pow(radius,2)

print("The area of the circle is: ", area)


# ___________________________________________________

# Circunference 
# circumference (c = 2 x pi x r)

ra = int(input("Enter the radius of the circle: "))

# formula
c = 2 * (PI * ra)

print("The Circumference of the Circle is: ", c)


#__________________________________________
##Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x = int(input("Enter your variable for  the operation : "))
y = pow(x,2) + (6 * x) + 9


print("When ",x," ten y is: ",y)



