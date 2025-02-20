import requests
import pandas as pd
import numpy as np
import os
import json
from PIL import Image
import matplotlib.pyplot as plt

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

path = os.path.join(os.getcwd(), 'addresses.csv')
response = requests.get(url)
with open(path, 'wb') as f:
    f.write(response.content)

df = pd.read_csv('addresses.csv', header=None)
print(df)

# Adding column name to the DataFrame
df.columns = ['First Name', 'Last Name', 'Location', 'City', 'State', 'Area Code']

# Selecting a single column
df['First Name']

# Selecting a multiple columns
df = df[['First Name', 'Last Name', 'Location', 'City','State','Area Code']]

# Selecting rows using .iloc and .loc

print(df.loc[0])
print(df.loc[0:3, "First Name"])
print(df.iloc[[0,1,2], 0])

# Transform Function in Pandas
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])

# Let’s say we want to add 10 to each element in a dataframe:
df = df.transform(func = lambda x : x + 10)

# Now we will use DataFrame.transform() function to find the square root to each element of the dataframe.
result = df.transform(func = ['sqrt'])
print(result)

# JSON to a File
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

# Serialization using dump() function

# json.dump() method can be used for writing to JSON file.
# Syntax: json.dump(dict, file_pointer)
# Parameters:
# 1. dictionary – name of the dictionary which should be converted to JSON object.
# 2. file pointer – pointer of the file opened in write or append mode.

with open('person.json', 'w') as f:
    json.dump(person, f)

# serialization using dumps() function
# json.dumps() that helps in converting a dictionary to a JSON object.
# It takes two parameters:
# 1. dictionary – name of the dictionary which should be converted to JSON object.
# 2. indent – defines the number of units for indentation

json_object = json.dumps(person, indent = 4) 
with open('sample.json', 'w') as outfile:
    outfile.write(json_object)
print(json_object)

# Reading JSON to a File
# The JSON package has json.load() function that loads the json content from a json file into a dictionary.
# File poniter: A file pointer that points to a JSON file

with open('sample.json', 'r') as openfile:
    json_object = json.load(openfile)
print(json_object)

# XLSX file format

file_xlsx = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"

path = os.path.join(os.getcwd(), 'file_example_XLSX_10.xlsx')
response1 = requests.get(file_xlsx)
with open(path, 'wb') as f:
    f.write(response1.content)

df = pd.read_excel('file_example_XLSX_10.xlsx')
print(df)

# Binary File Format

# Reading the Image file: PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities

filename_pil = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"

path = os.path.join(os.getcwd(), "./dog.jpg")
response_pil = requests.get(filename_pil)
with open(path, 'wb') as f:
    f.write(response_pil.content)

# Read the image
img = Image.open('./dog.jpg', 'r')
img.show()

# Data Analysis

# About this Dataset
# Context: This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years of age of Pima Indian heritage.
# Content: The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on. We have 768 rows and 9 columns. The first 8 columns represent the features and the last column represent the target/label.

filename_d = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

path_d = os.path.join(os.getcwd(), 'diabetes.csv')
response_d = requests.get(filename_d)
with open(path_d, 'wb') as f:
    f.write(response_d.content)
df_d = pd.read_csv('diabetes.csv')

# Selection of the 5 rows using dataframe.head() method
print(df_d.head(5))

# Dimension
print(df_d.shape)

# Statistical Overview of dataset
print(df_d.info())

# Pandas describe() is used to view some basic statistical details like percentile, mean, standard deviation, etc. of a data frame or a series of numeric values. When this method is applied to a series of strings, it returns a different output
print(df_d.describe())

# Identify and handle missing values
missing_data = df_d.isnull()
missing_data.head(5)

# Count missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

# Visualization
labels = 'Not Diabetic', 'Diabetic'
plt.pie(df_d['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()