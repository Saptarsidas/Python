# Create a recursive Python function to calculate the power of a number (x^n).
def power(base,num):
    if(num!=0):
        return( base * power(base,num-1))
    else:
        return 1
num1=int(input("Number"))
power1=int(input("Power"))
print("power of a number is",power(num1,power1) )

