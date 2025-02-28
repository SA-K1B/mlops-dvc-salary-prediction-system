import pandas as pd
df = pd.read_csv('data/raw/Salary_Data.csv')
print(df.head())
# print(df.info())
# print(df.describe())
print(df.isnull().sum())