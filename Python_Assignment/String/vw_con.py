# Count the number of vowels and consonants in a string.
str1=input("Please enter :")
vowels=0
consonants=0
for i in str1:
    if  (i=='A'or i==' E ' or i=='I'or i=='O' or i=='U'or i=='a'or i=='i'or i=='e'or i=='o'or i=='u'):
     vowels+=1
    else:
       consonants+=1

print("In  a string vowels are ",vowels)
print("In  a string consonants are",consonants)
