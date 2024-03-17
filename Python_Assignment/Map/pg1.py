# Write a python program that uses the map function to square each element of a list of numbers
element=[]
n=int(input("How many elements u want to insert :"))
for i in range(0,n):
    ele=int(input())
    element.append(ele)
print("The actual element are ", element)
def square(num):
    return num**2
new=(list(map(square,element)))
print("After square the elements are",new)