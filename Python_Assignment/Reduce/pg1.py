# # Write a python program that uses reduce function to find the product of all elements in a list
from functools import reduce

lst=[]
n=int(input("enter how many elemnets in a list :"))
for i in range (0,n):
    ele=int(input())
    lst.append(ele)
print(lst)
num1 =reduce(lambda x, y: x * y, lst)
print(num1)
