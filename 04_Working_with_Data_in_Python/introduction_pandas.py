import pandas as pd

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
dfCSV = pd.read_csv(csv_path)
df = pd.read_excel(xlsx_path)
x = df[['Length']]

# Quiz on DataFrame
q = df[['Rating']]

# Assign the variable q to the dataframe that is made up of the column Released and Artist:
q = df[['Released','Artist']]

# Access the 2nd row and the 3rd column of df:
q = df.iloc[1, 2]

# Use the following list to convert the dataframe index df to characters and assign it to df_new; find the element corresponding to the row index a and column 'Artist'. Then select the rows a through d for the column 'Artist'
new_index=['a','b','c','d','e','f','g','h']
df_new = df
df_new.index = new_index
df_new.loc['a', 'Artist']
print(df_new.loc['a' : 'd', 'Artist'])
