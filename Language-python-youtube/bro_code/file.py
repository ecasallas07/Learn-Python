# file detection in python
import os 
path = "C:\\Users\\ecasa\\OneDrive\\Documentos\\practice_pyton.txt"
# Exist validate files path
if os.path.exists(path):
    print("That location is correct")
    if os.path.isfile(path):
        print("That is file")
    elif os.path.isdir(path):
        print("That is directory")
else:
    print("That locatio is not correct")
    print(path)


# Read file with python
try:
    with open("text.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found:()")


text = "God is great, and he is live"
# options for read, writter file
with open("text.txt",'w') as file:
    file.write(text)

# option for copy file in python
# copyfile() = copies content of file
# copy() = copyefile() + permission mode + direction can be a directory
# copy2()= copy() + copies metada( file's creation adn modification times)

import shutil

shutil.copyfile('text.txt','copy.txt')

# moved file

source = "tezt.txt"
destination = "C:\\Users\\ecasa\\OneDrive\\Documentos\\text.txt"


try:
    if os.path.exists(source):
        print("there is alredy a file there")
    else:
        os.replace(source,destination)
except FileNotFoundError:
    print(source,"was not found")



# remove file

os.remove("text.txt")



#MODULES
#
# import <name_file>
# import <name_file> as file    
# from <name_file> import <function1>, <function2>
help("modules")
