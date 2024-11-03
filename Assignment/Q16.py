# 16. Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).
a = float (input("enter a side of triangle = "))
b = float (input("enter b side of triangle = "))
c = float (input("enter c side of triangle = "))
if a == b == c:
    print (f" triangle is equilateral ")
elif a == b or b == c or a == c:
    print (f" triangle is isosceles ")
else:
    print (f" triangle is scalene ")
