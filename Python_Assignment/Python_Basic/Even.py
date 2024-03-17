#Create a Python program that prints all even numbers from 1 to 20 using a for loop.
even=0
odd=0
for i in range(1,20+1):
    if (i%2==0): 
        even=even+i
    else:
        odd=odd+i
print(odd)
print( even)

