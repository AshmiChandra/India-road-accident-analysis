import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('clean_dataset.csv')

print(df.corr(numeric_only=True))
print(df.describe())
top10 = df.sort_values('Total_Cases', ascending=False).head(10)

plt.bar(top10['area'],top10['Total_Cases'], color='yellow')
plt.title("Top 10 areas of registered cases")
plt.show()

top10['Fatality_Rate'] = (top10['Total_Died'] / top10['Total_Cases']) * 100
plt.bar(top10['area'], top10['Fatality_Rate'], color='pink')
plt.title("Fatality Rate (%) - Top 10 States by Cases")
plt.xticks(rotation=45, ha='right')
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='Blues')
plt.title("Correlation Heatmap")
plt.show()

sns.scatterplot(data=df, x='Total_Cases', y='Total_Died')
plt.title("Cases vs Deaths by Area")
plt.show()

#print(df.size)