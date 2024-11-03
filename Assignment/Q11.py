# 11. Check if a given number is a multiple of both 3 and 5.
num = int(input("enter Number = "))
if num % 3 == 0 and num % 5==0:
    print (f" {num} is multiple of 3 and 5 ")
else:
    print (f" {num} is not multiple of 3 and 5 ")