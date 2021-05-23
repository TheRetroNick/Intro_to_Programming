# Import OS Mod
import os
import time

#print Current Directory
cwd = os.getcwd()
print("Current Working Directory:" ,cwd)
# Print directory list
listdir = os.listdir()
print('Directory List:', listdir)
# Take user input to change the directory
os.chdir(input('What directory do you want to save in? '))
# Print the new CWD
cwd = os.getcwd()
print("Current Working Directory:" ,cwd)
# Start creating a file
New = input("New file name? ")
# Input a file name

fh = open((New) +'.txt', 'w')
fh.write(input('What is your name? '))
fh.write(', ')
fh.write(input('Address? '))
fh.write(', ')
fh.write(input('Phone number? '))
fh.close()
print("File created - " +(New))
time.sleep(3)