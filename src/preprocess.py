import pandas as pd
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('data/raw/Salary_Data.csv')
print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())

# diplay unique values in each column
for col in df.columns:
    print(col, df[col].nunique())

# drop all the null values
df.dropna(inplace=True)
print(df.isnull().sum())
# apply standard scalar transformation

scaler = StandardScaler()
columns_to_scale = ['Salary', 'Years of Experience', 'Age']
for column in columns_to_scale:
    df[column] = scaler.fit_transform(df[[column]])
print(df.head())

df.to_csv('data/processed/processed_data.csv', index=False)
