num=int(input("Enter the number "))
digit=0
i=1
while i<=num:
    rem=num // 10
    digit+=1
    num /= 10
print(digit)