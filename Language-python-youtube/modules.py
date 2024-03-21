# import built -in modules
"""
    OS Module
    Sys Module
    Statistics Module
    Math Module
    String Module
    Random Module
"""

import mymodule
import os

print(mymodule.generate_full_name('Esteban','Casallas'))

# creating a directory
os.mkdir('directory_name')
#changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()