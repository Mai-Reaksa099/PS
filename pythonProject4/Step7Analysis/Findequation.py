import math
from Component.DataSet import data_ting
from Component.Pakage import Num
import numpy as np
import matplotlib.pyplot as plt

add = Num()

x = np.array([i[0] for i in data_ting])
y = np.array([i[1] for i in data_ting])
# find mean x and y
X_Mean = sum(x) / len(x)
Y_Mean = sum(y) / len(y)

print('Mean of X value ', round(X_Mean, 2))
print('Mean of Y value ', round(Y_Mean, 2))

# declare list x and y
ls_x = []
ls_y = []

for i in x:
    ls_x = x - X_Mean

print('==========================')
round_to_whole = [round(num, 3) for num in ls_x]
# print list of X- X bar
print('Value of X - X bar: ')
print(round_to_whole)
# print power of X - X bar
sqrt_on = np.power(round_to_whole, 2)
print('Power of Under as: ')
print(sqrt_on)
# Sum power X-X bar and print
sum_x = sum(sqrt_on)
round_to_sum_x = round(sum_x, 3)
print('=================================')
print('Sum of List X = ', round_to_sum_x)
# Find Y -Y bar
for i in y:
    ls_y = y - Y_Mean
print('===========================')
round_to_whole1 = [round(num, 2) for num in ls_y]
print('Value of Y - Y bar ')
print(round_to_whole1)

# find (X-X bar)(Y-Y bar)
products = []
for num1, num2 in zip(ls_x, ls_y):
    products.append(num1 * num2)

print('=================================')
round_to_product = [round(num, 2) for num in products]
# Print round Value of (X -X bar)(Y - Y bar)
print('Value of Multy (X - X bar)(Y - Y bar): ')
print(round_to_product)
# Sum of (X - X bar)(Y - Y abr)
sum_on = sum(round_to_product)
sum_on_round = round(sum_on, 2)
print('===========================')
# Print (X - X bar)(Y - Y abr)
print('Sum on For B as: ', sum_on_round)
print('===========================')


# multi = sum(products)
# round_to_multi = [round(num, 3) for num in multi]
# print('Multy of Sum X and Y = ', round_to_multi)
# round_to_multi = round(multi, 3)
# print('Multy of Sum X and Y = ', round_to_multi)
# Fin Value of B
b = sum_on_round / round_to_sum_x
print('Value of B in Linear: ', round(b, 2))

# Find A = y bar- b xbar

A = Y_Mean - (b * X_Mean)
print('Value of A : ', round(A, 2))
# Y^ = A + B(1/x)
# x = 'X'
# Y_Linear  = A + (B/x)

ls_Y_linear = []
for i in x:
    ls_Y_linear = A + b * (1/x)
Round_Y_hat = [round(num, 2) for num in ls_Y_linear]
print('Prin Y^ ')
print(Round_Y_hat)

# Float Graph Predicted Value
# plt.scatter(x, Round_Y_hat)
# plt.show()
# Find Residuals
ls_Re = []
for i in y:
    ls_Re = y - Round_Y_hat

Residuals_Round = [round(num, 2) for num in ls_Re]
print('Print Value Residuals as: ')
print(Residuals_Round)

# Find SSR
SSR = add.SSResid(y, Round_Y_hat)
print('Value SSR as: ', round(SSR, 2))
# Find SST
SST = add.SSTo(y)
print('Value SST as : ', round(SST, 2))
# Find Coefficient of determination
R_r = add.r_square(y, Round_Y_hat)
print('Value of R^ as ', R_r)
# Find Se
Se = math.sqrt(SSR/len(x) - 2)
print('Value of Se ', round(Se, 2))
# Transform Data
# Find X^
# X^ = A-Y^/b
X_bar = []
for i in Round_Y_hat:
    X_bar = (A - Round_Y_hat)/b

Round_X_bar = [round(num, 2) for num in X_bar]
print('Value of Transforming X^ For Analysis Graph')
print(Round_X_bar)
# Floating Graph
plt.scatter(Round_X_bar, Round_Y_hat)
plt.show()
