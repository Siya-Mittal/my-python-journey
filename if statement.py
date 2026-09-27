#if = Do some only IF condition is true
#     Else do something else 
age = int(input("Enter your age: "))


if age >= 18 :
    print ("You are eligible")
elif age < 0 :
    print("You are not born yet !")
elif age >= 100:
    print("You are too old!")   
else :
    print("You are not eligible")

# case 2

response = input("Would you like some food ? (Y/N)")

if response == "Y" :
    print("Have some food! ")
else : 
    print("No food for you!")    

# Case 3
name = input("Enter your name: ")    
if name == "":
    print("You didn't type in your name! ")
else:
    print(f"Hello {name}")    

#For boolean statement

for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("This item is Not for sale")

# 2
online = True
if online :
    print("This user is online")
else :
    print("This user is offline")

