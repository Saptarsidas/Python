# Create a python program that uses reduced to find the G C D of a list of numbers
from functools import reduce
lst=[]
n=int(input("enter how many elemnets in a list :"))
for i in range (0,n):
    ele=int(input())
    lst.append(ele)
print("The original list ",lst)
def gcd(a,b):
    if (b!=0):
        return gcd(b,a%b)
    else:
        return a
new=reduce(lambda x,y:gcd(x,y),lst)
print("Gcd of a list",new)