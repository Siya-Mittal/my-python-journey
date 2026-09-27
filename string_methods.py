# TO know other string methods use 
# print(help(str))

name = input("Enter your full name: ")
phone_no = input("Enter your phone no: ")

result = len(name)
result_2 = name.find(" ")
result_3 = name.rfind("i")
name = name.capitalize()
name_2 = name.upper()
name_3 = name.lower()
result_4 = name.isdigit()
result_5 = name.isalpha()
result_6 = phone_no.count("-")
phone_no = phone_no.replace("-"," ")


print(result)
print(result_2)
print(result_3)
print(name)
print(name_2)
print(name_3)
print(result_4)
print(result_5)
print(result_6)
print(phone_no)