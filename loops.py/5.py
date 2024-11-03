# 5. Print all odd numbers between 1 and 100 using a loop.
for i in range ( 1 , 101 , 1):
    print (f"odd numbers in for loop = {i}")
    if i % 2 != 0:
        print (f"odd numbers in for loop by Modulas method = {i}")
j = 0
while j < 100:
    j += 1
    if j % 2 != 0:
        print (f"odd numbers in while loop = {j}")
       