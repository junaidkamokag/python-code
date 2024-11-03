# 15. Write a program to check if a number is within a specified range.
start = int (input("Enter Start Number = "))
end = int (input("Enter end Number = "))
numb = int (input("Enter Number = "))
if start <= numb <= end:
    print (f"{numb} is in specified range")
else:
    print (f"{numb} is not in specified range")
 