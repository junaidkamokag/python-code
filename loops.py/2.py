# 12. Print all prime numbers between 1 and 50.
import math
number = int(input("Enter your Number = "))
# 1st squre root of number
# answer of squre root is loop lenght
# if all are devisible then its a prime number other wise not a prime number
squrRoot = int(math.sqrt(number))
for i in range(1,squrRoot+1,1):
    if squrRoot % i == 0:
        print(f"{number} is a prime number ")
    else:
        print(f"{number} is not a prime number ")