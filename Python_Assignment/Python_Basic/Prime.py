
n=int(input("enter the number"))
flag=0
if n > 1:
    for i in range(2,(n//2)+1):
        if (n%i)==0:
            flag=1
        break
    if (flag==0):
        print("prime number")
    else:
         print("not prime ")