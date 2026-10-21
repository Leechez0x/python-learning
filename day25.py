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