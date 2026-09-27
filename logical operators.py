# logical operators = evaluate multiple conditions (or, and ,not)
#                or = at least one condition must be true 
#               and = both condition must be true 
#               not = inverts the condition (not false , not true)
 
temp = 90
is_raining = False

if temp > 35 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# 2
is_sunny = False

if temp >= 22 and is_sunny:
    print("It's HOT outside")
    print("It's SUNNY ")
elif temp <= 0 and is_sunny:
    print("It's COLD outside")
    print("It's SUNNY ")
elif temp < 28 and temp > 0 and is_sunny:
    #temp < 28 and temp > 0 can be written as 28 > temp >0
    print("It's WARM outside")
    print("It's SUNNY ")
elif temp >= 22 and not is_sunny:
    print("It's HOT outside")
    print("It's CLOUDY ")
elif temp <= 0 and not is_sunny:
    print("It's COLD outside")
    print("It's CLOUDY ")
elif temp < 28 and temp > 0 and not is_sunny:
    #temp < 28 and temp > 0 can be written as 28 > temp >0
    print("It's WARM outside")
    print("It's CLOUDY ")
