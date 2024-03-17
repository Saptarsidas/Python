# #Create a Python program that prints the Fibonacci sequence up to a specified limit using a for loop.
# num=int(input("enter a number"))
# n1=0
# n2=1
# sum=0
# if num<=0:
#     print("enter number greater number than 0")
# else:
#     for i in range(0,num):
#         print(sum,end= ' ')
#         n1=n2
#         n2=sum
#         sum=n1+n2

#Create a Python program that prints the Fibonacci sequence up to a specified limit using a while loop.
num=int(input("enter a number"))
n1=0
n2=1
sum=0
i=0
while i<num:
    print(n1)
    sum=n1+n2
    n1=n2
    n2=sum
    i=i+1

