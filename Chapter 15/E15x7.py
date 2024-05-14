# Program E15x7.py
# Line chart
import matplotlib.pyplot as plt
import pandas as pd
df= pd.read_csv("E:/Py programs/50_Startups.csv")
# get columns to plot
columns = df.columns.drop(['State'])
# create x data
x_data = range(0, df.shape[0])
# create figure and axis
fig, ax = plt.subplots()
# plot each column
for column in columns:
    ax.plot(x_data, df[column])
# set title and legend
ax.set_title('50_Startups')
ax.legend(['R&D Spend', 'Administration',  'Marketing Spend', 'Profit'])
plt.show()
