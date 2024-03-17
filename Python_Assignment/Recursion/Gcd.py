# Create a recursive Python function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
def gcd(a,b):
    if (b!=0):
        return gcd(b,a%b)
    else :
        return a
x=int(input("enter the no:"))
y=int(input("enter no:"))
print (gcd(x,y))