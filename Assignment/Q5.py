# 5. Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).
person = float (input("Enter your grade:"))
con = "congratulation"
if person > 100:
    print ("Enter correct persontage ! ")
elif person <0:
    print("Enter correct persontage ! ")
elif person > 90:
    print (f"{con} your score is {person} % you are awarded with A grade")
elif person > 80 and person < 90:
    print (f"{con} your score is {person} % you are awarded with B grade")
elif person > 70 and person < 80:
    print (f"{con} your score is {person} % you are awarded with C grade")
elif person > 60 and person < 70:
    print (f"{con} your score is {person} % you are awarded with D grade")
else:
    print(f"your score is {person}your garade is F you need to improve your studies")
print ("++++++++++++++++++++++++++++++++++++++++++")
