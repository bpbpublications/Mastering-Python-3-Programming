# Program E15x4.py
# Scatter plot using pandas
import matplotlib.pyplot as plt
import pandas as pd
df= pd.read_csv("E:/Py programs/50_Startups.csv")
df.plot.scatter(x='R&D Spend', y='Profit', title='50_Startups')
plt.show()
