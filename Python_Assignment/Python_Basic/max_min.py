lst1 = [10,5,2,4,7,9,55,4,66,]
max=lst1[0]
min=lst1[0]
for n in lst1:
    if n>max:
        max=n
    if n<min:
        min=n
print("maximum value is",max )
print("Minimum values is", min)