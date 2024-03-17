# Count the occurrences of a word in a string.
Str1=input("Enter a string :")
w=input("Enter a word that will be search :")
count=0
words=Str1.split()

for i in words:
    if i == w:
        count+=1

print("The word apper  in the string.",count)