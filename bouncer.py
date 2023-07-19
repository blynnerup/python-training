# Bounces you based on age
# ask for age
age = input("How old are you: ")

if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband")
    # 18 -21 wristband
    elif age >= 21:
        print("You are good to enter and can drink!")
    # 21+ drink, normal entry
    else: 
        print ("Too young! ")
    # too young
else:
    print("Please enter an age")