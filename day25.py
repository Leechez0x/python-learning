import pandas as pd

nums = [1,2,3,4,5]
s = pd.Series(nums)
print(s)

fruits = pd.Series ([10,20,30], index=['apple', 'banana', 'mango'])
print(fruits)
print(fruits['banana'])

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25,30,35,28],
    'country': ['USA', 'UK', 'Canada', 'Austrailia']
}

df = pd.DataFrame(data)
print(df)
print(df.head())        # first 5 rows
print(df.tail())        # last 5 rows
print(df.shape)         # (rows, columns)
print(df.info())        # column names, data types, count
print(df.describe())    # statistics for number columns


print (df['name'])
print(df[['name', 'age']])


# Filtering rows
print(df['age'] > 28)           # rows where age is greater than 28
print(df['country'] == 'USA')   # rows where country is USA

# Filtering rows
print(df[df['age'] > 28])           # rows where age is greater than 28
print(df[df['country'] == 'USA'])   # rows where country is USA