"""
Function
________
def function_name(parameters):
    doc string
    statements
    ...

"""
#======== Program 01: Define a function ===========

def welcome():
    '''this is my first function :'''
    print('Hello, Towhid Islam. Good morning')

welcome()
print(welcome.__doc__)  # It will return the Document Section



#======== Program 02: Define function with parameter =============

def welcome1(name):
    print(f'Hello,{name}. Good Morning!!')

welcome1('Tawhidul Islam')

def welcome2(name, msg):
    print(f'Hellow,{name}. {msg}!!')

welcome2('Ayman Ferdous Jaman','Good Evening')
welcome2('Ayman Ferdous Jaman','Good Afternoon')


#======== Program 03: Define function with Default value in parameter =============

def welcome3(n='Reem Hossain',m='Good Night'):
    print(n,m)

welcome3()
welcome3('Ceaser','Tumi kemon acho')



#======== Program 04: Define function with parameter & in PRINT pass any string=============
def welcome4(x,y,z):
    print('Hellow',x)
    print('Hellow',y)
    print('Hellow',z)





#======== Program 05:Define function by using Star(*)Parameter ===========

def welcome5(*names): #Here star(*) is Lists of items.
    for x in names:
        print('Hello..!',x)

welcome5('Salam','Anzam','Reem','Ceasar') #Because of using Star(*) we can pass more than one value in parameter.


# def double(x):
#     return(x*2)
    
    
# z=double(3)
# print(z)

# print(double(10))


#========= Program 06: Lambda Function============
# Alternative Way Using Lambda Function()
# Syntax for Lambda --> FunctionName=lambda Arguments: Expression

double=lambda x: x*2

print(double(10))



#========= Program 08: Lambda Function with Double Star(**)Parameter =============
def buildProfile(**user_info): #Two/Double stars(**) stands for Dictionary.
    profile={}
    for key,value in user_info.items():
        profile[key]=value

    return profile

userProfile=buildProfile(name='Ceasar', address='Lima-Peru', field='IT')
print(userProfile)


#========= Program 08: Arithmetic Operation ===========

def add(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print(add(5,6))
print(sub(15,6))
print(mul(2,6))
print(div(10,3))




