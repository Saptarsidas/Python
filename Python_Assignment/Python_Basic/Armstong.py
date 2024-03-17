num=int(input("enter the number"))
l=[]
digitcount=0
sum=0
arm=num
while(num>=1):
    rem=num%10
    l.append(rem)
    digitcount+=1
    num=num//10
print(digitcount)
for item in l:
    sum+=item**digitcount
print(sum)

if(arm==sum):
    print("Number is Armstong")
else:
    print("Number is not Armstong")
