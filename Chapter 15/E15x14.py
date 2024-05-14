# Program E15x14.py
# Scatter plot using pandas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df= pd.read_csv ("E:/Py programs/50_Startups.csv")
sns.scatterplot(x='R&D Spend', y='Profit', data=df)
plt.title('50_Startups')
plt.show()
