from Component.DataSet import data_ting
import numpy as np
import matplotlib.pyplot as plt

x = np.array([i[0] for i in data_ting])
y = np.array([i[1] for i in data_ting])

plt.scatter(x, y)
plt.show()
