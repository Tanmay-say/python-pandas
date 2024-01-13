import pandas as pd
import random

dict1 = {
   "Name"  : [f"Student {i} " for i in range(0 ,10)],
   "Age"   : [random.randint(18 ,25) for _ in range(10)],
   "Number" : [random.randint(7000000000 , 9999999999) for _ in range(10)]
}
df1 = pd.DataFrame(dict1 )

cities = ["Nagpur ", "Delhi ", "Kolkata" , "Chennai"]
dict2 = {
    "Name"  : [f"Student {i} " for i in range(10 ,20)],
   "City"   : [random.choice(cities) for _ in range(10)],
   "Salary" : [random.randint(100000,200000) for _ in range(10)]
}
df2 = pd.DataFrame(dict2 )

country = ["India " , "Africa" , "Usa" , "Uk" ]
dict3 = {
    "Country"  : [random.choice(country) for _ in range(10)],
}
df4 = pd.DataFrame(dict3 )




df3 = pd.concat([df1,df2,df4],ignore_index= True)   #append not working so concat is used

df3 = df3.fillna('////')
print(df3)