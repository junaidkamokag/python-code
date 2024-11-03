# 17. Write a program that continues to ask for a number until the correct number is guessed.
correct_number = 12
while True:
    guess = int(input("enter your number = "))

    if guess == correct_number:
        print ("you Guessed a corrected number")
        break
    else:
        print("wrong number Re-Enter number")
        # guess = int(input("enter your number = "))
    