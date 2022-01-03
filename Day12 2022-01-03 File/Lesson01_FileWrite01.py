'''
File 
--------
The syntax to open a file object in Python

Syntax:
file_object=open("FileName","mode")

Modes are: 
1. 'r'    - Read mode (Default)
2. 'w'    - Write mode
3. 'a'    - Append
4. 'r+'   - Special Read & Write Mode.


'''
#====== Program 01: To create a file and access different modes. ====
file=open("testfile.txt",'w') #Write Mode
# file.write("Hello World...!!")
# file.write("This is our new text file")
# file.write("And this is another line")



file.write("Hello World...!!\n")
file.write("This is our new text file\n")
file.write("And this is another line\n")
file.close()


file=open("testfile.txt",'a') #Append Mode
file.write("This is from Append Mode...!")
file.close()


