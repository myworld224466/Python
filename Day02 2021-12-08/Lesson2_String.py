s="hAve a nice dAy"
print(s)


print(s.upper()) #Upper of all character
print(s.lower()) #Lower of all character
print(s.title()) #Only the Camel cases make upper
print(s.capitalize()) #Only the first letter of the line will upper
print(s.swapcase()) #If caharacters are lower make it upper and if charecters are in upper makes it lower
print(s.center(60)) #Margin from left is 60 pxls.
print(s.center(60,'*')) #Margin center with character * Left and Right. (Even on Right & Odd on Left)
print('m'.center(2,'*'))
print('me'.center(3,'*'))
print('me'.center(4,'*'))
print('me'.center(5,'*'))
print('123456'.center(11,'*'))


print(s.replace('nice','good')) # Replace Targeted word with New word
print(s.find('nice')) #To find the index position of a character
print(s.index('nice')) #To find the index position of a character
print(s.count('a')) # To count how many specified character are available in the sentance.
print(s.count('a')) # To count how many specified character are available in the sentance.
print(s.lower().count('a')) # First convert to lower and than count the specified word in a string
print(s.split()) #It will separate the total string in group of words
s2='We, love, python, programming, language'
print(s2.split(','))


s3='We love-python programming language'
print(s3.split('-'))

result=s2.split(',')
print(result)
print(type(result))
print(type(s2))
print(dir(s))