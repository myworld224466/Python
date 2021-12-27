# #=========Program to print Prime Number of a given range ==========
# x=int(input("Enter the range of numbers :"))
# print("The prime numbers are: ")
# for p in range(1,x):
#     isPrime=True
#     for i in range(2,p):
#         if p%i==0:
#             isPrime=False
#             break
#     if isPrime:
#         print(p,end=" ")




#=========Program to print Prime Number of a given range ==========
def prime(x,y):
    print("The prime numbers are: ")
    for p in range(x,y):
        isPrime=True
        for i in range(2,p):
            if p%i==0:
                isPrime=False
                break
        if isPrime:
            print(p,end=" ")

a=int(input("Enter the Starting Range :"))
b=int(input("Enter the Ending Range :"))
prime(a,b)


