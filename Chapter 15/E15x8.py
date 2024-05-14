# Program E15x8.py
# line chart using pandas
import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv("E:/Py programs/50_Startups.csv")
df.drop(['State'], axis=1).plot.line(title='50_Startups')
plt.show()
