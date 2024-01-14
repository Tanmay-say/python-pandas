import pandas as pd
from scipy.stats import zscore

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Charlie', 'Alice', 'Bob'],
    'Age': [25, 30, None, 22, 28, 35, None, 30],
    'Salary': [50000, 60000, 55000, 48000, None, 60000, 52000, 62000],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'San Francisco', 'Chicago']
}

df = pd.DataFrame(data)

# Display the original dataset
print("Original Dataset:")
print(df)
print("\n")

# Handling Missing Values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Removing Duplicate Entries
df_cleaned = df.drop_duplicates()

# Standardizing Text Data
df['City'] = df['City'].str.lower()

# Handling Outliers
z_scores = zscore(df_cleaned['Salary'])
df_no_outliers = df_cleaned[(z_scores < 3) & (z_scores > -3)]

# Correcting Data Types
df_no_outliers['Age'] = df_no_outliers['Age'].astype(int)
df_no_outliers['Salary'] = df_no_outliers['Salary'].astype(int)

# Replacing Values
city_mapping = {'new york': 'NY', 'san francisco': 'SF', 'los angeles': 'LA', 'chicago': 'CHI'}
df_no_outliers['City'] = df_no_outliers['City'].replace(city_mapping)

# Display the cleaned dataset
print("Cleaned Dataset:")
print(df_no_outliers)
