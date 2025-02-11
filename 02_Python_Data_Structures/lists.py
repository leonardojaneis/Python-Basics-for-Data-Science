# Quiz on List

# Create a list a_list, with the following elements 1, hello, [1,2,3] and True.
a_list = [1, "hello", [1,2,3], True]

# Find the value stored at index 1 of a_list.
print(a_list[1])

# Retrieve the elements stored at index 1, 2 and 3 of a_list.
print(a_list[1:4])

# Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:
A = [1, 'a']
B = [2, 1, 'd']
C = A + B
print(C)

# Scenario : Shopping List

# Task-1 Create an empty list
shopping_list = []

# Task-2 Now store the number of items to the shopping_list (Watch, Laptop, Pen, Shoes, Clothes)
shopping_list = ["Watch", "Laptop", "Shoes", "Pen", "Clothes"]

# Task-3 Add a new item to the shopping_list (Footbal)s
shopping_list.extend(["Football"]) # or shopping_list.append("Football")

# Task-4 Print First item from the shopping_list
print(shopping_list[0])

# Task-5 Print the last item from the shopping_list
print(shopping_list[-1]) # or print(shopping_list[5])

# Task-6 Print the entire shopping_list
print(shopping_list)

# Task-7 Print the item that are important to buy from the Shopping List (Laptop and Shoes)
print(shopping_list[1:3])

# Task-8 Change the item from the shopping_list (Pen to Notebbok)
shopping_list[3] = "Notebook"

# Task-9 Delete the item from the shopping_list thath is not required (Clothes)
del(shopping_list[4])

# Task-10 Print the entire shopping_list
print(shopping_list)