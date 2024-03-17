# Write a python program that uses the filter function to select even numbers from a list of integers
lst=[]
n=int(input("Enter  how many elements u want to inserts : "))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print("The current list ",lst)
def even(n):
    return n%2==0
new=list(filter(even,lst))
print("even list is",new)