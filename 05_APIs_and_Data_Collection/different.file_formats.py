import requests
import pandas as pd
import os

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

path = os.path.join(os.getcwd(), 'addresses.csv')
response = requests.get(url)
with open(path, 'wb') as f:
    f.write(response.content)

df = pd.read_csv('addresses.csv', header=None)
print(df)

# Adding column name to the DataFrame
