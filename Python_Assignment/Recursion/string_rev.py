# Write a recursive Python function to reverse a string
def rev(str):
    if len(str) ==0:
        return str
    else:
        return rev(str[1:])+str[0]
str1=input("Please enter a string")
print (rev(str1))