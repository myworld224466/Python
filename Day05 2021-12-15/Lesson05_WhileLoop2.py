
'''#Program continus loop and Key for exit
while True:
    msg=input("Enter the message: ")
    if msg=='x':
        break
    print(msg)
'''

'''
#Program to print sumation of sequence 10 numbers (1+2+3+4+5+6+7+8+9+10= 55)
i=1
sum=0
while i<=10:
    #sum=sum+s
    print(i,end='+')
    if i==10:
        print(i,end=' ')
    sum+=i
    i+=1

print("=",sum)'''



'''
#Print using Back Space (\b) to eliminate the repeat + sight after 10
i=1
sum=0
while i<=10:
    print(i,end='+')
    sum+=i
    i+=1
print("\b=",sum)

'''

#Print using If - Else to eliminate the repeat + sight after 10
i=1
sum=0
while i<=10:
    if i==10:
        print(i,end=' ')
    else:
        print(i,end='+')
    sum+=i
    i+=1

print("=",sum)

