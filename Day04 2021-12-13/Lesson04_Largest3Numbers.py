#Find the Largest between 3 numbers

try:
    print('Enter the values:')
    x=int(input('Enter the First number X: '))
    y=int(input('Enter the Second number Y: '))
    z=int(input('Enter the Third number Z: '))

    if x>=y and y>=z:
        print('The largest number is X')
    elif y>=x and y>=z:
        print('The largest number is Y')
    else:
        print('The largest number is Z')
except Exception as ex:
    print(ex)
    print('Invalid input please try again..!!')