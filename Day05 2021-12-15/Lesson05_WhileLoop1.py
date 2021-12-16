'''
While loop
---------------
init variable
while <condition>:
    statements
    ......
'''
'''#To print from 1 to 5 in Column
x=1
while x<=5:
    print(x)
    x+=1


#To print from 1 to 5 in Row
x=1
while x<=5:
    print(x,end=' ')
    #For END='' it will print on row side by side.
    #We can assign any value / symbol in end='@@'
    x+=1 #Compund assignment operator
'''
#Program to print numbers sequence given by users
sv=int(input('Enter Start Value :'))
ev=int(input('Enter End Value :'))
# print(f'The range from {sv} to {ev} Even numbers are: ')
# while sv<=ev:
#     if(sv%2==0):
#         print(sv,end=' ')
#     sv+=1
# print('\n')


print(f'The range from {sv} to {ev} Odd numbers are: ',)
while sv<=ev:
    if(sv%2!=0):
        print(sv,end=' ')
    sv+=1