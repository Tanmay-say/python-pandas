import pandas as pd
import random

dict1 = {
   "Name"  : [f"Student {i} " for i in range(0 ,20)],
   "Age"   : [random.randint(18 ,40) for _ in range(20)],
   "Number" : [random.randint(7000000000 , 9999999999) for _ in range(20)]
}
df1 = pd.DataFrame(dict1 )
print(df1)

average_grade_by_student = df1.groupby('Name')['Age'].median()

print(average_grade_by_student)