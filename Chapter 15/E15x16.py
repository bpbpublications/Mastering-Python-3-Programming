# Program E15x16.py
# histogram - Gaussian Kernel Density Plot using seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv('C:/Users/Subbu/Desktop/winesreview.csv')
sns.histplot(df['points'], bins=10, kde=True)
plt.xlabel('points')
plt.ylabel('frequency')
plt.title ('Wines Review')
plt.show()
