# Create a python program uses the reduce function to concatenate a list of string into a single string
from functools import reduce
lst=[]
n=int(input("Enter how many elementes you want to insert :"))
for i in range(0,n):
    ele=input()
    lst.append(ele)
print(lst)
str1=reduce(lambda x,y: x+" "+y,lst)
print(str1)