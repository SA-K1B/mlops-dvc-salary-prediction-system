import pandas as pd
df = pd.read_csv('data/raw/Salary_Data.csv')
# print(df.head())
print(df.info())
# print(df.describe())
print(df.isnull().sum())

# diplay unique values in each column
# for col in df.columns:
#     print(col, df[col].nunique())

# drop all the null values
df.dropna(inplace=True)
# print(df.isnull().sum())

# save the dataset
df.to_csv('data/processed/processed_data.csv', index=False)