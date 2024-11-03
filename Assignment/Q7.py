# 7. Write a program to find the largest of three numbers.
num_1 = int(input("Enter your 1st Number = "))
num_2 = int(input("Enter your 2nd Number = "))
num_3 = int(input("Enter your 3rd Number = "))
if num_1 > num_2 and num_1 > num_3:
    print (f"the large number is {num_1}")
elif num_2 > num_1 and num_2 > num_3:
    print (f"the large number is {num_2}")
else:
    print (f"the large number is {num_3}")
print("++++++++++++++++++++++++++++++++++++++++++++++++")
