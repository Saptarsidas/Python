# Write a python program that calculates the map function to round each element of a list of floating point numbers to the nearest integer
element=[]
n=int(input("How many elements u want to insert :"))
for i in range(0,n):
    ele=float(input())
    element.append(ele)
print(element)
def nearest_int(num):
    return round(num)
new=(list(map(nearest_int,element)))
print(new)