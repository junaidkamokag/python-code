# 2. Take a user’s age as input and display whether they are a minor, adult, or senior citizen.
age = float(input("Enter your age :"))
if age < 18:
    print ("You are Minor")
elif age >= 18 and age <=64:
    print ("Your are adult")
else:
    print ("you are senior Citizen")
print ("+++++++++++++++++++++++++++++++++++++++++++++++++")