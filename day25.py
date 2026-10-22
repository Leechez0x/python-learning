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

df['salary'] = [50000, 60000, 70000, 55000]
df = df.drop('salary', axis=1)
print(df)


import csv 

with open('students.csv', 'w', newline= '') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'score'])
    writer.writerow(['Alice', 20, 85])
    writer.writerow(['Bob', 22, 90])
    writer.writerow(['Charlie', 21, 78])
    writer.writerow(['David', 23, 95])

df2 = pd.read_csv('students.csv')
print(df2)

print(df2.sort_values('score'))
print(df2.sort_values('score', ascending=False))