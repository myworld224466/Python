#Program to conduct task by selecting Menu number:

while True:
    print("Main Menu: ")
    print('1. Adition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit')
    print('Please enter your selection from the Menu: ')

    x=input()
    if x=='1':
        a=int(input('Please enter the value for A: '))
        b=int(input('Please enter the value for B: '))
        print (f'Adition of {a} + {b} is: ''%s'%(a+b))
        print('\n')
    elif x=='2':
        a=int(input('Please enter the value for A: '))
        b=int(input('Please enter the value for B: '))
        print (f'Subtraction of {a} - {b} is: ''%s'%(a-b))
        print('\n')
    elif x=='3':
        a=int(input('Please enter the value for A: '))
        b=int(input('Please enter the value for B: '))
        print (f'Multiplication of {a} * {b} is: ''%s'%(a*b))
        print('\n')
    elif x=='4':
        a=int(input('Please enter the value for A: '))
        b=int(input('Please enter the value for B: '))
        print (f'Division of {a} / {b} is: ''%s'%(int(a/b)))
        print('\n')
    elif x=='5':
        print ('Thank you, Bye.')
        break
    else:
        print ('Please enter a valid number from Menu.')