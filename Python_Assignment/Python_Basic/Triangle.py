#Create a Python program that identifies the type of a triangle (e.g., equilateral, isosceles, or scalene) based on input values using if-else.
s1=int(input("Enter side of triangle-"))
s2=int(input("Enter side of triangle-"))
s3=int(input("Enter side of triangle-"))
if s1==s2 and s2==s3:
     print("Triangle is equilateral")
elif s1==s2!=s3 or s2==s3!=s2 or s1==s3!=s2:
     print("Triangle is isosceles")
else:
    print("Triangle is scalene")