# Create a recursive Python function to find the nth Fibonacci number.
def Fibonacci(n):
        if n==0:
          return 0
        elif n==1:
           return 1
        else:
            return (Fibonacci(n-1)+Fibonacci(n-2))
n=int(input("NUMBER BOL BHAAIIIIIIIIII JALDIIIIIIII::::"))
for i in range(n):

    print(Fibonacci(i))
    
