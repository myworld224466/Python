#====Program 02: Create a file and use various file functions() ==========

file=open("testfile.txt",'r')
#print(file.readlines()) #This will read the total lines & will convert to List
#lines=file.readlines()
# for x in lines:
#     print (x)


#====Program 03: Read entire file==========
#print(file.read())


#====Program 04: Read number of character as defined by user ==========
# print(file.read(25))


#====Program 04: To read a single line ==========
# print(file.readline()) 

sl=1
for x in file:
    print(sl,'.',x)
    sl+=1



file.close()