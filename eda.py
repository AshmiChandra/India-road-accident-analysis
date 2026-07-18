import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('clean_dataset.csv')

print(df.corr(numeric_only=True))
print(df.describe())
print(df.sort_values('Total_Cases', ascending=False).head(12))
print(df.sort_values('Total_Died', ascending=False).head(12))

#print(df.size)