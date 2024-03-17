def sum_n(n):
    if n == 0:
        return 1
    else:
         result= n+sum_n(n-1)
         return result
n=int(input("enter a no :"))
print(sum_n(n))