import pandas as pd

# Provided data set
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Subject': ['Math', 'Math', 'Math', 'English', 'English', 'English'],
    'Grade': [85, 90, 78, 92, 88, 76]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Grouping by 'Name' and calculating the mean
average_grade_by_student = df.groupby('Name')['Grade'].mean()

# Convert the Series to a DataFrame
average_grade_df = average_grade_by_student.reset_index(name='Average Grade')

# Save the DataFrame to a CSV file
average_grade_df.to_csv('average_grade_by_student.csv', index=False)
print(average_grade_df)
