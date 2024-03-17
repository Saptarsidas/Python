# Write a python program that uses a filter function to select prime numbers from a list of integers
lst=[]
n=int(input("Enter  how many elements u want to inserts : "))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print("The current list ",lst)
def prime(num):
    for i in  range(2,int(num**0.5)+1):
         if num%i==0:
             return False
    return True
new=list(filter(prime,lst))
print("prime list is",new)