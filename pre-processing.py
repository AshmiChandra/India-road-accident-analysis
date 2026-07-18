import pandas as pd
import numpy as np

df = pd.read_csv('dataset.csv')

print(df.head())
print(df.info())
print(df.describe())
print(df.columns)

# # handling null values
print(df.isnull().sum())

# handling duplicates
print(df.duplicated().sum())

#renaming
df.rename(columns={'Sl. No.' : 's_no', 'State/UT/City': 'area', 
        'Road Accidents - Cases': 'Road_Cases', 'Road Accidents - Injured': 'Road_Injured', 
        'Road Accidents - Died': 'Road_Died', 'Railway Accidents - Cases': 'Railway_Cases', 
        'Railway Accidents - Injured': 'Railway_Injured', 'Railway Accidents - Died': 'Railway_Died', 
        'Railway Crossing Accidents - Cases': 'Railway_Crossing_Cases', 
        'Railway Crossing Accidents - Injured': 'Railway_Crossing_Injured', 
        'Railway Crossing Accidents - Died': 'Railway_Crossing_Died', 
        'Total Traffic Accidents - Cases': 'Total_Cases',
       'Total Traffic Accidents - Injured': 'Total_Injured', 
       'Total Traffic Accidents - Died': 'Total_Died'},inplace= True)
print(df.columns)

#make sure no non numeric vals and covertiung if needed
print(df.dtypes)
df['s_no'] = pd.to_numeric(df['s_no'],errors='coerce')
print(df.dtypes)

df.to_csv('clean_dataset.csv', index=False)

#EDA starts