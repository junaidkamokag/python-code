# 12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.
temperature = int(input("enter temperature in ° C = ") )
if temperature < 14:
    print (f"weather at {temperature} °C is freezing ")
elif temperature >= 15 and temperature <= 25:
    print (f"weather at {temperature} °C is moderate ")
else:
    print (f"weather at {temperature} °C is hot ")