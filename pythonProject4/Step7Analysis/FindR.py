# R is simple correlation coefficient
from Component.DataSet import data_ting
from Component.Pakage import Num
import numpy as np
import matplotlib.pyplot as plt

add = Num()
x = np.array([i[0] for i in data_ting])
y = np.array([i[1] for i in data_ting])

r = add.r([i[0] for i in data_ting], [i[1] for i in data_ting])
print('Sample Correlation Coefficient = ', r)



