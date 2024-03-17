def prime(n):
    for i in range(2,n):
        if (n%i == 0):
            print("  NOT prime")
            break
    else:
        print(" prime")
n=int(input("enter the number "))
prime(n)