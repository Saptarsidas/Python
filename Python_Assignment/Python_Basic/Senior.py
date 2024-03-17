# Create a Python program that determines the eligibility of a person for a senior citizen discount based on age using if-else.

age=int(input("enter age : "))

if(age!=10):
    amnt=int(input("Enter the amount : "))
    if(age>=18 and age<=25):
        discnt=amnt*0.02
    elif(age>=26 and age<=35):
        discnt=amnt*0.05
    elif(age>=36 and age<=45):
        discnt=amnt*0.07
    elif(age>=46 and age<=60):
        discnt=amnt*0.09
    elif(61<=age):
        discnt=amnt*0.10

    print("Discount is :",discnt)
    print("Total cost : ",amnt-discnt)
else:
    print("You're not 18 so you don't get discount....sorry!! ")