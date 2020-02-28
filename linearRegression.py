import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# Prepare Data
x = 10*np.random.rand(100)
y = 3*x+np.random.rand(100)
print(x,y)
plt.scatter(x,y)
plt.show()
