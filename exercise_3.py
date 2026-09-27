# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces 
# 3. username must not contain digits

username = input("Enter a usename: ")

if len(username) > 12 :
    print("username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("username can't contain spaces")
elif not  username.isalpha():
    print("username can not contain digits")
else:
    print(f"Welcome {username}")