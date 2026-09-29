# format specifiers = {value :flags} format a value based on what flags are inserted 

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces 
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value 
# :  = insrt a space before positive numbers 
# :, = comma separator
price1 = 348809.14159
price2 = -9808877.65
price3 = 19852.34
print(f"price1 is {price1:.2f}")
print(f"price2 is {price2:.2f}")
print(f"price3 is {price3:.2f}")

print(f"price1 is {price1:10}")
print(f"price2 is {price2:10}")
print(f"price3 is {price3:10}")

print(f"price1 is {price1:010}")
print(f"price2 is {price2:010}")
print(f"price3 is {price3:010}")

print(f"price1 is {price1:<10}")
print(f"price2 is {price2:<10}")
print(f"price3 is {price3:<10}")

print(f"price1 is {price1:>10}")
print(f"price2 is {price2:>10}")
print(f"price3 is {price3:>10}")

print(f"price1 is {price1:+}")
print(f"price2 is {price2:+}")
print(f"price3 is {price3:+}")

print(f"price1 is {price1: }")
print(f"price2 is {price2: }")
print(f"price3 is {price3: }")

print(f"price1 is {price1:,}")
print(f"price2 is {price2:,}")
print(f"price3 is {price3:,}")

print(f"price1 is {price1:+,.2f}")
print(f"price2 is {price2:+,.2f}")
print(f"price3 is {price3:+,.2f}")



