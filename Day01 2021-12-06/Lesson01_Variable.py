'''
Date: 06/Dec/2021 
Prepared by: Ceasar
Topics : Variables
'''
print("This is the first Lesson")
print('Welcome to my Python World..!!!')

# Declare variables Control+Front Slash to make comments automatically a line.
name="Joe Biden"
age=79
country='USA'
isActive=True
# The numeric value need convert to string by using the str() function in front of the Variable.
print("Name of the USA president is "+name+" and his age is "+str(age)+ " Years old")

# %s significant as a String value, this is a syntax similar to C program.
print("President of USA is %s and his age is %s"%(name,age))

# We can use {Index Value} and the end need to mention key word format(Variable Name)
print("President of {0} is {1} years old".format(name,age))

print("---- Without index value ------")
print("President of {} is {} years old".format(name,age))

# We can use {Index Variable Name} but at the beging of "Double Cotation" should declare small "f"
#This is known as Python format to get output
print(f"President of {country} is {age} years old.")