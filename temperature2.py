# necessary import libraries
import numpy as np
import datetime, time
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

# dummy inputs (one day)
data = [10.0, 11.1, 12.3, 13.2, 14.8, 15.6, 16.7, 17.5, 18.9, 19.7, 20.7, 21.1, 22.6, 23.5, 24.9, 25.1, 26.3, 27.8,
        28.8, 29.6, 30.2, 31.6, 32.1, 33.7]
train = [34.38, 34.36, 34.74, 35.26, 35.23, 35.29, 35.64, 36.02, 36.1, 36.98, 37.01, 36.75, 36.01, 35.66, 34.72, 33.9,
         32.62, 31.51, 30.73, 29.5, 26.94, 25.47, 23.84, 22.55]
test = [36.02, 36.1, 36.98, 37.01, 36.75, 36.01, 35.66, 34.72, 33.9, 32.62, 31.51, 30.73, 29.5, 26.94, 25.47, 23.84,
        22.55, 21.03, 19.92, 18.77, 18.48, 18.07, 17.91, 17.11]
startDate = '2013-01-01'
endDate = '2013-01-01'
p = 1
n = 1
print(len(data), len(train), len(test))


# utility function
def predictTemperature(startDate, endDate, temperature, n):
    p = int(len(temperature) / 24)
    x = []
    for i in range(1, ((24 * p) + 1)):
        x.append(i)
    y = temperature
    plt.plot(x, y)
    plt.show()
    lm = LinearRegression()
    lm.fit(np.asarray(x).reshape(-1, 1), y)

    f = x[-1] + 1
    z = []
    for i in range(24 * n):
        z.append(f)
        f += 1
    return (lm.predict(np.asarray(x).reshape(-1, 1)).tolist())


# call the utility function
print(predictTemperature(startDate, endDate, train, n))