
#leap year check
year=int(input("Enter the Year"))
if year%4==0 and year%100!=0 or year%100==0:
    print(" Leap year")
else:
    print(" Not leap year ")