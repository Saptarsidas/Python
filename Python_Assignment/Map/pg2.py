# Create a python program that uses the map function to convert a list of names to upper case
lst=[]
n=int(input("How many namess u want to insert :"))
for i in range(0,n):
    lst1=input()
    lst.append(lst1)
print(lst)
def case(name):
    return name.upper()
new=(list(map(case,lst)))
print(new)