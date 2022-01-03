#==== Program 05: Make a directory and Validation being exist======
import os

try:
    os.mkdir("tempdir") #To create a directory
except Exception as ex:
    # print('File already exist..!',ex.args[1])# 1=> Error message & 0=> Error code
    print(ex.args[1])# 1=> Error message & 0=> Error code

# os.chdir("tempdir") #To change a directory

print(os.getcwd()) #The method os. getcwd() in Python returns the current working directory of a process.


# os.rmdir("tempdir")

if os.path.exists("testfile.txt"):
    os.remove("testfile.txt")
else:
    print("File doesn't exist..!")

