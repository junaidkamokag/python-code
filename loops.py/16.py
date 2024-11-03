# 16. Create a program to calculate the sum of the digits of an inputted integer.
num = int (input ("enter number = "))
num_to_str = str(num)
for i in num_to_str:
    srt_i_int = int(i)
    sum = srt_i_int + srt_i_int
    print (f"i = {i} and sum = {sum}")
