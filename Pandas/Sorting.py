import pandas as pd
import random

dict1 = {
   "Name"  : [f"Student {i} " for i in range(0 ,20)],
   "Age"   : [random.randint(18 ,40) for _ in range(20)],
   "Number" : [random.randint(7000000000 , 9999999999) for _ in range(20)]
}

df = pd.DataFrame(dict1)
df.to_csv('Before_Sort.csv', index=False)
df = df.sort_values('Age')
df.to_csv('After_Sort.csv', index=False)
print(df)

