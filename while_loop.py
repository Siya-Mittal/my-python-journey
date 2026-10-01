# while loop = execute some code WHILE  some condition remains true

name = (input("Enter your name: "))
age = int(input("Enter your age: "))
food = input("Enter a food u like (q to quit): ")
num =  int(input("Enter a num between 1-10" ))

while name == "":
    print("You didn't enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")

while not food == "q":
    print(f"you like {food}")
    food = input("Enter another food u like (q to quit): ")
print("bye")

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a num between 1-10" ))
print(f"Your no is {num}")

