#Create a Python program that checks if a given year is a century year or not using if-else.
year=int(input("enter a year"))

def is_century(year):
    if year<=100:
        print("1st century")
    elif year%100==0:
        print(year//100,"century")
    else :
        print( year//100+1,"century")

is_century(year)