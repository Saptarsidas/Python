num=int(input("Enter the number "))
i=1
rev=0
while i<=num:
    rem=num%10
    rev=(rev*10)+rem
    num//=10
print(rev)