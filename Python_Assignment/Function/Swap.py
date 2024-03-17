def  f1():   
    print("Hello")   
f1()    
print(f1())

# # swap two numbwer
def swap(x,y): 
    x,y = y,x
    return x,y
x=int(input("Enter a number") )
y=int(input("Enter a number"))
swap(x,y) 
print ("swap is ",swap(x,y))

#sum of variable argument values
def sum(*a):
    sum=0
    for i in a:
        sum=sum + i
    print("sum is ",sum)
sum()
sum(10)
sum(123,324,255)

# for normal variable arguments the container is a tuple.
# for keyword variable argument is a dictionary