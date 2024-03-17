# Create a python program that uses map function to convert the list of temperatures from Celsius to Fahrenheit
lst=[]
n=int(input("enter the number of list :"))
for i in range (0,n):
    ele=int(input())
    lst.append(ele)
print(lst)
def convert_temp(num):
    f=(num*9/5)+32
    # c=5/9*(num-32)
    return f
new=(list(map(convert_temp,lst)))
print(new)