# Write a python program that uses the map function to calculate the length of each word in a list of a string
lst=[]
n=int(input("How many namess u want to insert :"))
for i in range(0,n):
    lst1=input()
    lst.append(lst1)
print(lst)
new=list(map(len,lst))
print(new)