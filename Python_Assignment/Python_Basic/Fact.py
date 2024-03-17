#Write a Python program that calculates the factorial of a number using a for loop.
n=int(input("Enter a number: "))
fact=1
#backward
for i in range(n,1,-1):
#forward        
#for i in range(1,n+1):
        fact=fact*i
print("factorial is",fact)