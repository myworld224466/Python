#==== Program 06: Factorial of a number by using Recursive function ===
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))




#==== Program 07: Fibonacci Series using Recursive function === 
def fibonacci(n):
    if n==0:
        return [0]
    elif n==1:
        return [0,1]
    else:
        fibo=fibonacci(n-1)
        nextElement=fibo[n-1]+fibo[n-2]
        fibo.append(nextElement)
        return fibo

print(fibonacci(6))



#==== Program 08: Check Prime number using Recursive function ===
def checkPrime(n,i=2):
    if n==i:
        return True
    else:
        if n%i==0:
            return False
        else:
            return checkPrime(n,i+1)

print(checkPrime(16))