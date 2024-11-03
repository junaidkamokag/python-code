# 10. Write a program to determine if a given character is a vowel or consonant.
character = str(input("enter character = ")).lower()
if character in "aeiou":
    print (f"{character} is vowel")
else:
    print (f"{character} is not vowel")