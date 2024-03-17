# Write a Python program that defines a function to calculate the sum of two numbers and then calls the function.
def add(a,b):
    print("sum of two elements",(a+b))
a=int(input("Enter the numbers :"))
b=int(input("Enter the numbers :"))
add(a,b)
# Create a Python function that takes two arguments and returns their product
def adding(a,b):
    return a+b
print("sum of two numbers")
print(adding(10,20))

# Create a Python function that accepts a variable number of arguments and calculates their sum.
def add1(L):
    total=0
    for i in L:
        total +=i
    print(total)
L=[10,20,30,40,50,60,70,80,90,100]
add1(L)
