# Program E15x3.py
# Scatter plot
import matplotlib.pyplot as plt
import pandas as pd
df= pd.read_csv("E:/Py programs/50_Startups.csv")
# create a figure and axis
fig, ax = plt.subplots()

# scatter the R&D Spend and Profit
ax.scatter(df['R&D Spend'], df['Profit'])
# set a title and labels
ax.set_title('50_Startups')
ax.set_xlabel('R&D Spend')
ax.set_ylabel('Profit')
plt.show()
