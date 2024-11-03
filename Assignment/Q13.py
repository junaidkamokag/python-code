# 13. Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.
num1 = int (input("enter 1st number = "))
num2 = int (input("enter 2nd number = "))
operator = input("Enter Operator + - / * ")
if operator == "+" :
    print (num1 + num2)
elif operator == " - ":
    print (num1 - num2)
elif operator == " // ":
    print (num1 // num2)
elif operator == " * ":
    print (num1 * num2)
else :
    print ("Nothing")