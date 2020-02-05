#ask for age
age = input("How old are you? ")

#18-21 wristband
if int(age) >= 18 and int(age) <= 21:
    print("You can enter but you have to wear a wristband. ")

# 21+ drink
elif int(age) >= 21:
    print("You are good to enter and can drink. ")

#too young, sorry
else:
    print("You are too young to enter. ")
    
