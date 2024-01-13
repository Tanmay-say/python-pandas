import pandas as pd
import random

dict1 = {
   "Name"  : [f"Student {i} " for i in range(0 ,10)],
   "Age"   : [random.randint(18 ,25) for _ in range(10)],
   "Number" : [random.randint(7000000000 , 9999999999) for _ in range(10)]
}
cities = ["Nagpur ", "Delhi ", "Kolkata" , "Chennai"]
dict2 = {
    "Name"  : [f"Student {i} " for i in range(0 ,10)],
   "City"   : [random.choice(cities) for _ in range(10)],
   "Salary" : [random.randint(100000,200000) for _ in range(10)]
}

df1 = pd.DataFrame(dict1 )
df2 = pd.DataFrame(dict2 )

df3 = pd.merge(df1,df2,on='Name', how='inner') #Colum should be similar

print(df3)