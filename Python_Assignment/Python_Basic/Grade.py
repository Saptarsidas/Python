#Create a Python program that determines the grade of a student based on their score using if-else.
#100-91= O,81-90=E,71-80=A,61-70=B,51-60=C,41-50=D,BELOW 40=FAIL
sub1=(int(input("Enter the number")))
sub2=(int(input("Enter the number")))
sub3=(int(input("Enter the number")))
sub4=(int(input("Enter the number")))
sub5=(int(input("Enter the number")))
total=(sub1+sub2+sub3+sub4+sub5)
avg=total/5
print("Total",total)
print("Average",avg)
if avg>=91 and avg<=100:
        print("O")
elif avg>=81 and avg<=90:
        print("E")
elif avg>=71 and avg<=80:
        print("A")
elif avg>=61 and avg<=70:
        print("B")
elif avg>=51 and avg<=60:
        print("C")
elif avg>=41 and avg<=50:
        print("D")
else:
        print("Fail")