#User Login
'''
IF -> ELSE
IF -> ELIF -> ELSE
'''

u=input('Enter the user name: ')
p=input('Enter the password: ')


#Program 1 (IF->ELSE):
"""
if u.upper()=='Admin'.upper():
    if p=='123':
        print(f'Welcome Mr.{u}')
    else:
        print('Invalid password!!!')
else:
    print('Invalid User Name')

"""

#Program 2 (IF->ELIF->ELSE):
if u.upper()=='Admin'.upper() and p=='123':
    print('Welcome...!!')
elif u.upper()!='Admin'.upper() and p=='123':
    print('Wrong User Name!!')
elif u.upper()=='Admin'.upper() and p!='123':
    print('Wrong Password!!')
else:
    print('Please verify your User Name and Password ')


