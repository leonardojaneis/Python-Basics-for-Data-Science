# Python provides a built-in module called re, which allows you to work with regular expressions. First, import the re module
import re 

# Quiz on Strings

# What is the value of the variable "a" after the following code is executed?
a = "1"
print(a)

# What is the value of the variable "b" after the following code is executed?
b = "2"
print(b)

# What is the value of the variable "c" after the following code is executed?
c = a + b
print(c)

# Consider the variable "d" use slicing to print out the first three elements:
d = "ABCDEFG"
print(d[0:3])

# Use a stride value of 2 to print out every second character of the string e:
e = 'clocrkr1e1c1t'
print(e[::2])

# Print out a backslash:
print("\\")

# Convert the variable "f" to uppercase:
f = "You are wrong"
print(f.upper())

# Convert the variable "f2" to lowercase:
f2 = "YOU ARE RIGHT"
print(f2.lower())

# Consider the variable "g", and find the first index of the sub-string snow:
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
print(g.find("snow"))

# In the variable "g", replace the sub-string Mary with Bob:
print(g.replace("Mary", "Bob"))

# In the variable "g", replace the sub-string , with .:
print(g.replace(',', '.'))

# In the variable "g", split the substring to list:
print(g.split())

# In the string "s3", find whether the digit is present or not using the \d and search() function:
s3 = "House number- 1105"
result = re.search(r"\d", s3)
if result:
    print("Digit found")
else:
    print("Digit not found")

# In the string "str1", replace the sub-string fox with bear using sub() function:
str1 = "The quick brown fox jumps over the lazy dog."
new_str1 = re.sub("fox", "bear", str1)
print(new_str1)

# In the string str2 find all the occurrences of woo using findall() function:
str2 = "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
result = re.findall("woo", str2)
print(result)