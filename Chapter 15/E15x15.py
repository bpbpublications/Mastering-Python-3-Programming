# Program E15x15.py
# histogram using seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv('C:/Users/Subbu/Desktop/winesreview.csv')
sns.histplot(df['points'], bins=10, kde=False)
plt.xlabel('points')
plt.ylabel('frequency')
plt.title ('Wines Review')
plt.show()
