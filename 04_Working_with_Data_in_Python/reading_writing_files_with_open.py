import os
import requests
import pandas as pd
from random import randint as rnd
'''
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"


def download(url, filename):
    if os.path.exists(filename):
        print("O arquivo já existe!")
        return
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

download(url, "example1.txt")
print("Done")

# Reading the file
example1 = "example1.txt"
file1 = open(example1, "r")
print(f"Path of file: {file1.name}") # Printing the path of file
print(f"Mode of file: {file1.mode}") # Printing the mode of file

# Assign it to a variable
FileContent = file1.read()
print(FileContent)
file1.close() # Closing the file

# Using with to open a File in a better way
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Reading certain amount of chacacters
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

# Read on line
with open(example1, "r") as file1:
    print(file1.readline(20))

# Iterate trough the lines
with open(example1, "r") as file1:
    i = 0
    for line in file1:
        print("Iteration", str(i), ":", line)
        i = i + 1

# Reaad all lines and save as a list
with open(example1, 'r') as file1:
    FileAsList = file1.readlines()
print(FileAsList[1])

# Writing Files
exmp2 = 'example2.txt'
with open(exmp2, 'w') as writeFile:
    writeFile.write("This is line A\n") 
    writeFile.write("This is line B\n")      

# Write a list to a .txt file
Lines = ["This is line A \n", "This is line B\n", "This is line C\n"]
with open(exmp2, 'w') as writeFile:
    for line in Lines:
        writeFile.write(line)

# Appending Files
with open(exmp2, 'a') as testWriteFile:
    testWriteFile.write("This is line C\n")  
    testWriteFile.write("This is line D\n")  
    testWriteFile.write("This is line E\n")  
'''

# Exercise
# Your local university's Raptors fan club maintains a register of its active members on a .txt document. Every month they update the file by removing the members who are not active. You have been tasked with automating this with your Python skills. Given the file currentMem, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the exMem file. Make sure that the format of the original files in preserved. (Hint: Do this by reading/writing whole lines and ensuring the header remains) Run the code block below prior to starting the exercise. The skeleton code has been provided for you. Edit only the cleanFiles function.

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))

    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))

genFiles(memReg,exReg)

'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
'''

def cleanFiles(currentMem, exMem):
    with open(currentMem, 'r+') as writeFile:
        with open(exMem, 'a+') as appendFile:
            writeFile.seek(0)
            members = writeFile.readlines()
            header = members[0]
            members.pop(0)
            inactive = [member for member in members if ('no' in member)]
            writeFile.seek(0) 
            writeFile.write(header)
            for member in members:
                if (member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)      
            writeFile.truncate()

cleanFiles(memReg,exReg)

headers = "Membership No  Date Joined  Active  \n"

with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

testWrite = "testWrite.txt"
testAppend = "testAppend.txt" 
passed = True

genFiles(testWrite,testAppend)

with open(testWrite,'r') as file:
    ogWrite = file.readlines()

with open(testAppend,'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite,testAppend)
except:
    print('Error')

with open(testWrite,'r') as file:
    clWrite = file.readlines()

with open(testAppend,'r') as file:
    clAppend = file.readlines()
        
# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False
    
for line in clWrite:
    if  'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does not match original file")
            passed = False
print ("{}".format(testMsg(passed)))