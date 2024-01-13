import pandas as pd
import random

# Generate a simple dataset for 20 students
dict = {
    'Name': [f'Student {i}' for i in range(1, 21)],
    'Age': [random.randint(18, 25) for _ in range(20)],
    'Marks': [random.randint(60, 100) for _ in range(20)],
    'M_Number': [random.randint(7000000000,9999999999) for _ in range(20)]
}

# Create a DataFrame
df = pd.DataFrame(dict )

high_marks_students = df[df['Marks'] > 80]
print(high_marks_students)