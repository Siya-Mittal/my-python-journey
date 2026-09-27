import math
radius = float(input('Enter the radius of a circle'))

 
circumference = 2 * math.pi * radius

print(f"The circumference of the circle is : {circumference}")
print(f"The circumference of the circle is : {round(circumference, 2)}cm")

Area = math.pi * pow(radius, 2)

print(f"The area of the circle is : {Area} cm²")

print(f"The area of the circle is : {round(Area, 2)}cm²")

a = float(input("Enter side A : "))
b = float(input("Enter side B : "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"side C = {c}")



