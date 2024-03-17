# create a python program that  uses reduce to find the maximum elements in the list
from functools import reduce
lst=[]
n=int(input("Enter how many elementes you want to insert :"))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(lst)
maxi=reduce(lambda x,y:x if  x>=y else y,lst)
print(maxi)
