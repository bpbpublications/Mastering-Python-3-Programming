# Program E15x6.py
# Scatter plot
# scatter plot of Administration Spend and Profit
import matplotlib.pyplot as plt
import pandas as pd
df= pd.read_csv("E:/Py programs/50_Startups.csv")
# create a figure and axis
fig, ax = plt.subplots()

# scatter the R&D Spend and Profit
ax.scatter(df['Administration'], df['Profit'])
# set a title and labels
ax.set_title('50_Startups')
ax.set_xlabel('Administration')
ax.set_ylabel('Profit')
plt.show()
