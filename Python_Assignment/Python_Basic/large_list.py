#Write a Python program to find the largest&smallest number in a list using a for loop.
mylist=[10,20,30,40 ,50,60]
large=mylist[0]
small=mylist[0]
for i in mylist:
    if i>large:
        large =i
    elif i<small:
        small =i
print('largest',large)
print('smallest',small)