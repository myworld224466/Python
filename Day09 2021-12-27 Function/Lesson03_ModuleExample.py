#======Program 10: We will call/import from other program ===========
'''
Here we will describe two methods to use the functions
1. By Function Name
2. By Using Star (*)
'''

#Method 01: Call by Function Name:
# from Lesson02_Calculator import add,sub,mul,div

#Method 02: Call by Using Star (*):
from Lesson02_Calculator import *

print(add(50,100))
print(sub(40,10))
print(mul(5,10))
print(div(40,10))
