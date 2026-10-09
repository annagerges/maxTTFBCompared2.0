import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("latency_data.csv")

mu=df['TTFB'].mean()
sigma=df['TTFB'].std()

#create a vector x that comprises of 600 points from the min to max ttfb values
x=np.linspace(df['TTFB'].min(),df['TTFB'].max(), 600)


#Gausian function
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) **2)

#plot the vector and Gausian function
plt.plot(x,y)

plt.title('Gausian Curve Of TTFB Data Points')
plt.xlabel('TTFB (ms)')
plt.ylabel('Probality Distribution')
plt.show()


