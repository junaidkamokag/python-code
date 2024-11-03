# 7. Find the factorial of a number using a while loop.
num = int(input("Enter your number = "))
fac = 1
i = 1
while i <= num:
    fac *= i
    i += 1
    print ("fac = ", fac)