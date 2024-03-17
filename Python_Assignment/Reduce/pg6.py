# Write a python program that uses the reduce function to find the sum of digits of a given number
from functools import reduce
lst=[]
n=int(input("enter how many elemnets in a list :"))
for i in range (0,n):
    ele=int(input())
    lst.append(ele)
print("The original list ",lst)
# while(n>0):
#     m=n%10
#     sum=sum+m
#     n=n//10
num=reduce(lambda x,y: x+y,lst)
print(num)