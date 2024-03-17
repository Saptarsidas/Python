#Create a Python program that generates a multiplication table for a given number using a for loop.
num=int(input("enter a number : "))
for i in range(1,num+1):
    print(num,"*",i,"=",num*i)