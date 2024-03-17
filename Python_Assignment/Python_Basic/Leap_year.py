#Create a Python program that checks if a given year is a leap year using both if-else and a function.

year=int(input("enter a year"))
def leapyear(year):
    if year%400==0 or year%100!=0 and year%4==0:
        print("Leap year",year)
    else:
        print(" Not Leap year",year)
leapyear(year)