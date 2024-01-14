import pandas as pd

# Sample dataset
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

# Data Cleaning and Exploration
# Handling Missing Values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Removing Duplicate Entries
df_cleaned = df.drop_duplicates()

# Provide a Summary of the Dataset
summary = df_cleaned.describe(include='all')

# Display the cleaned dataset
print("Cleaned Dataset:")
print(df_cleaned)
print("\n")

# Display the summary of the cleaned dataset
print("Summary of the Cleaned Dataset:")
print(summary)
