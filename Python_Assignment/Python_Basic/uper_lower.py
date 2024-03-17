#Write a Python program to categorize a given character as uppercase, lowercase, or neither using if-else.
ch=(input("Enter character :------------------------"))
if ch >= 'A' and ch <= 'Z':
    print("Uppercase")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase")
else:
    print("no case")