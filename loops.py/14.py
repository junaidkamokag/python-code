# 14. Write a program that breaks the loop when a certain condition is met.
score = int(input("enter number = "))
for i in range(score + 1):
    if score == i:
        print ("Thank you")
        break
    else:
        print("the code is running")
        