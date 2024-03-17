# Remove all whitespaces from a string.
# using replace method
Str1=input("Give  a string :")
Str1=Str1.replace(" ", "")
print(Str1)

# using split and join method   
Str1=input("Give  a string :")
Str1="".join(Str1.split())
print(Str1)