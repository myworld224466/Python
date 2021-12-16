#Sumation of Fibonacci series n!=0 1 1 2 3 5 8 13 21 34

# #========== Fibonacci program 1 ==========
# a=0
# b=1
# while b<=200:
#     print(a,b,end=" ")
#     a=a+b
#     b=b+a
# print("")


# ##==========Fibonacci program 2 ==========

# a,b=0,1
# while b<=200:
#     print(b,end='\t')
#     a,b=b,b+a



#========== Program Factorial of given number ( 4!=4*3*2*1=24) ==========

n=int(input('Please enter a number :'))
p=n
r=1
while n>=1:
    r=r*n
    print(n,end='*')
    n-=1
print('\b =',r)


