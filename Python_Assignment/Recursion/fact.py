# Write a Python program to calculate the factorial of a number using recursion.
def factorial(n):
    if n==0:
        result=1
    else:
       result=n*factorial(n-1)
    return result
n=int(input("Enter a number :"))
print(factorial(n))