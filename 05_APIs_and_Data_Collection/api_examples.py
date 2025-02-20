# Example 1: RandomUser API

from randomuser import RandomUser
import pandas as pd
import requests
import json

# Creating a random user object, r
r = RandomUser()

# Then, using generate_users() function, we get a list of random 10 users.
some_list = r.generate_users(10)

# The "Get Methods" functions can generate the required parameters to construct a dataset. For example, to get full name, we call get_full_name() function.
name = r.get_full_name()

# Let's say we only need 10 users with full names and their email addresses. We can write a "for-loop" to print these 10 users.
for user in some_list:
    print(user.get_full_name(), " ", user.get_email())

# Exercise 1
# In this Exercise, generate photos of the random 10 users.
for user in some_list:
    print(user.get_picture())

# To generate a table with information about the users, we can write a function containing all desirable parameters. For example, name, gender, city, etc. The parameters will depend on the requirements of the test to be performed. We call the Get Methods, then, we return pandas dataframe with the users.

def get_users():
    users = []
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
    return pd.DataFrame(users)

# Now we have a pandas dataframe that can be used for any testing purposes that the tester might have.
df1 = pd.DataFrame(get_users())

# Example 2: Fruityvice API
data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")

# Retrieving results using json.loads() function
results = json.loads(data.text)

# Converting the json data into pandas dataframe
pd.DataFrame(results)

# The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(results)

# Let's see if we can extract some information from this dataframe. Perhaps, we need to know the family and genus of a cherry.
cherry = df2[df2['name'] == 'Cherry']
family = cherry.iloc[0]['family']
genus = cherry.iloc[0]['genus']
print(f"Cherry family: {family}, Genus: {genus}")

# Exercise 2
# In this Exercise, find out how many calories are contained in a banana.
banana = df2[df2['name'] == 'Banana']
cal_banana = banana.iloc[0]['nutritions.calories']
print(f"Banana has {cal_banana} calories")

# Exercise 3 
# Official Joke API
url1 = 'https://official-joke-api.appspot.com/jokes/ten'

# 1. Using requests.get("url") function, load the data from the URL.
data1 = requests.get(url1)
# 2. Retrieve results using 'json.loads()' function.
results = json.loads(data1.text)
# 3. Convert json data into *pandas* data frame. Drop the type and id columns.
df3 = pd.DataFrame(results)
df3.drop(columns=['id', 'type'], inplace=True)
print(df3)