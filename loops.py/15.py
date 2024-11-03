# 15. Print the sum of even and odd numbers separately up to a given number.
for i in range(1,20,1):
    if i % 2 == 0:
        print (f"the toral of even Number = {i}")

for i in range(1,20,1):
    if i % 2 != 0:
        print (f"the toral of odd Number = {i}")
    
num = list(range(1,21))
even = 0
odd = 0
for i in range(len(num)):
    if num[i] % 2 == 0:
        even += num[i]
    else:
        odd += num[i]
print (f"even in list = {even} and odd in list = {odd}")