import pandas as pd

# Problem 1: Create a dataframe to display the result as below:
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

df = pd.DataFrame(x)


# Exercise 2: loc() and iloc() functions
# Use the loc() function,to get the Department of Jane in the newly created dataframe df1.
df1 = df
df1 = df1.set_index('Name')
#print(df1.head())
print(df1.loc['Jane', 'Salary']) 
print(df1.loc['Jane', 'Department'])
# 'Jane' salaty with iloc
print(df1.iloc[2, 2])

# Exercise 3: Slicing
# Using loc() function, do slicing on old dataframe df to retrieve the Name, ID and department of index column having labels as 2,3
print(df.loc[2:3, 'Name':'Department'])
