import math
def arm(n):
    sum=0
    k=n
    rem=0
    m=dcount(n)
    while(n>0):
        rem=n%10
        sum+=pow(rem,m)
        n=n//10
    print(sum)
    if sum==k:
        print("armstrong")
    else:
        print(" not armstrong")
    
def dcount(n):
    count=0
    while(n>0):
        n=n//10
        count+=1
    return count
    # print(count)
n=int(input("enter the number "))
arm(n)



