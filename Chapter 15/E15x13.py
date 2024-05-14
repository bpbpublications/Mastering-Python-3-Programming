# Program E15x13.py
# bar chart using pandas
import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv('C:/Users/Subbu/Desktop/winesreview.csv')
df['points'].value_counts().sort_index().plot.bar(title='wines Review')
plt.xlabel('points')
plt.ylabel('frequency')
plt.show()
