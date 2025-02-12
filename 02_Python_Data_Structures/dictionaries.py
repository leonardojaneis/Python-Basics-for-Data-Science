# Quiz on Dictionaries

soundtrack_dic = {"The Bodyguard": "1992", "Saturday Night Fever": "1977"}

# In the dictionary soundtrack_dict what are the keys?
print(soundtrack_dic.keys())

# In the dictionary soundtrack_dict what are the values?
print(soundtrack_dic.values())

# The Albums Back in Black, The Bodyguard and Thriller have the following music recording sales in millions 50, 50 and 65 respectively:
# Create a dictionary album_sales_dict where the keys are the album name and the sales in millions are the values.
album_sales_dict = {"Back in Black": 50, "The Bodyguard": 50, "Thriller": 65}

# Use the dictionary to find the total sales of Thriller:
album_sales_dict["Thriller"]

# Find the names of the albums from the dictionary using the methor keys():
album_sales_dict.keys() 

# Find the values of the recording sales from the dictionary using the method values:
album_sales_dict.values()

# Scenario: Inventory Store

# Task-1 Create an empty dictionary
inventory = {}

# Taks-2 Store the first product details in variable
product_name = "Mobile phone"
product_quantity = 5
product_price = 2000
product_rel_year = 2020

# Task-3 Add the details in inventory
inventory["Product Name"] = product_name
inventory["Quantity"] = product_quantity
inventory["Price"] = product_price
inventory["Release Year"] = product_rel_year

# Task-4 Store the second product details in variable
product_name2 = "Laptop"
product_quantity2 = 10
product_price2 = 50000
product_rel_year2 = 2023

# Task-5 Add the item detail into the inventory
inventory["Product Name2"] = product_name2
inventory["Quantity2"] = product_quantity2
inventory["Price2"] = product_price2
inventory["Release Year2"] = product_rel_year2

# Task-6 Display the Products present in the inventory
print(inventory)

# Task-7 Check if Release Year and Release Year2 is in the inventory
print("Release Year" in inventory)
print("Release Year2" in inventory)

# Task-8 Delete release year of both the products from the inventory
del(inventory["Release Year"])
del(inventory["Release Year2"])
