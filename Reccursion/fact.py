def factorial(n):      #factorial of number
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))    #fib series Number

def fib(n):
    if (n==0 or n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(5))