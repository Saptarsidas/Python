# Write a python program that calculates the factorial of a number using the reduce function
from functools import reduce
def fact(num):
        return reduce(lambda x,y:x*y,range(1,num+1))
num1=int(input("Enter a no "))
print(fact(num1))