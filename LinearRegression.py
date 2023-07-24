
import numpy as np;
import pandas as pd;

def line(x):
    return 5*x +8
size = 300
x = pd.Series(np.arange(size))
y = x.map(line) + np.random.randn(size)*10

df = pd.DataFrame({'X': x, 'Y': y})
import matplotlib.pyplot as plt

#plt.plot(df['X'], df['Y'])
#plt.show()

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(df[['X']], df['Y'])

ri = [12, 34]

print(model.coef_, '-----', model.intercept_)

def prediction(w0, w1, x):
    return x*w1 + w0


W1 = [20, 3, 43, 231, 2]
W0 = [0, 22, 34, 304, 8]
y_predicted = {}
for i in range(len(W1)):
    y_predicted['{}--{}'.format(W1[i], W0[i])] = prediction(W1[i], W0[i], i)

print(y_predicted)
print(y_predicted.values())

plt.plot(x[:5], y_predicted.values())
plt.show()