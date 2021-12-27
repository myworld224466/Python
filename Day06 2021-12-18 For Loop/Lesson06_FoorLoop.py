#For Loop
'''
Syntax:

for item in collection:
    statement
'''
#=========== Program for LIST ==============
# x=list(range(10))
# print(x)
# print("-"*50)
# y=list(range(10,50))
# print(y)
# print("-"*50)
# z=list(range(50,10,-1))
# print(z)
# print("-"*50)
# m=list(range(10,50,3))
# print(m)
# print("-"*50)

# #========= Program LIST:02 ============
# for x in ["apple","mango","banana","orange"]:
#     print(x)

# #========= Program LIST:03 ============

# fruits=["apple","mango","banana","orange"]
# for x in fruits:
#     print(x)


# #========= Program LIST:04 ============

# fruits=["apple","mango","banana","orange"]
# for x in fruits:
#     print(x[2])


#=========== Program FOR LOOP Print from 1 to 100==============
# for x in range(1,100+1):
#     print(x,end=" ")

# #=========== Program FOR LOOP Print Odd and Even Numbers==============
# for x in range(25,100):
#     if x%2==0:
#         print(x, end=" ")





#=========== Program FOR LOOP ==============
# for i in range(65,91):
#     #print (i)
#     print(chr(i))



# #=========== Program FOR LOOP  (Find Factorial of 4!)==============
# result=1
# for x in range(1,5):
#     result*=x
# print("Factorial of 4! is:", result)



# #=========== Program FOR LOOP  (print("-"*30))==============

# for x in range(30):
#     print("-",end="")



# #=========== Program FOR LOOP  Sum of Series 5=1+2+3+4+5=15==============
# x=int(input("Enter the value for Series :"))
# sum=0

# for y in range(x+1):
#     sum+=y
# print(sum)





# #=========== Program FOR LOOP  ASCII value of a Given Number==============
# x=int(input("Enter the Range to get ASCII value: "))
# for y in range(x+1):
#     print(chr(y),end=" ")




# #=========== Program FOR LOOP  ASCII value of a Given Number==============
# #==== Ex. 65=A, 66=B Ord=Ordinal value .
# #ord is oposite of chr

# x=input("Enter the Character to get ASCII equivalent value: ")
# print(ord(x),end=" ")


# #=========Program For Loop  To view a string in delay mode==================
# import time
# for j in "i love python":
#     print(j, end=" ",flush=True)
#     time.sleep(1)



# #========= Program For Loop: Prime number ===================
# #Ex. 17 = Prime, 9=Not Prime

# x=int(input("Enter Value :"))
# for i in range(2,x):
#     if x%i==0:
#         print("not prime")
#         break
#     else:
#         print("prime")
#         break




#========= Program For Loop: Prime number Using Boolean ===================
#Ex. 17 = Prime, 9=Not Prime

x=int(input("Enter Value :"))
isPrime=True
for i in range(2,x):
    if x%i==0:
        isPrime=False
        break

if isPrime:
    print("It's a Prime Number.")
else:
    print("It's not a Prime Number.")