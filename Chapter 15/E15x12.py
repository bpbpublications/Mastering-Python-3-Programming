# Program E15x12.py
# histogram using pandas
import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv('C:/Users/Subbu/Desktop/winesreview.csv')
df['points'].plot.hist(title='Wines evaluation')
plt.show()
