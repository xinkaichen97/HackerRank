# PROBLEM LINK : https://www.hackerrank.com/challenges/temperature-predictions

import numpy as np
from sklearn import ensemble
from sklearn.linear_model import LinearRegression


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def func(x, p1, p2, p3):
    return p1 * np.sin(p2 * x + p3) + 10


m = {"January": 0, "February": 1, "March": 2, "April": 3, "May": 4, "June": 5, "July": 6, "August": 7, "September": 8,
     "October": 9,
     "November": 10, "December": 11}
#n = int(input())
#input()
mins = []
maxs = []
x = []
testx = []
inputs = ['1908\tJanuary\t5.0\t-1.4',
          '1908\tFebruary\t7.3\t1.9',
          '1908\tMarch\t6.2\t0.3',
          '1908\tApril\tMissing_1\t2.1',
          '1908\tMay\tMissing_2\t7.7',
          '1908\tJune\t17.7\t8.7',
          '1908\tJuly\tMissing_3\t11.0',
          '1908\tAugust\t17.5\t9.7',
          '1908\tSeptember\t16.3\t8.4',
          '1908\tOctober\t14.6\t8.0',
          '1908\tNovember\t9.6\t3.4',
          '1908\tDecember\t5.8\tMissing_4',
          '1909\tJanuary\t5.0\t0.1',
          '1909\tFebruary\t5.5\t-0.3',
          '1909\tMarch\t5.6\t-0.3',
          '1909\tApril\t12.2\t3.3',
          '1909\tMay\t14.7\t4.8',
          '1909\tJune\t15.0\t7.5',
          '1909\tJuly\t17.3\t10.8',
          '1909\tAugust\t18.8\t10.7']
for i in range(len(inputs)):
    line = inputs[i].split('\t')
    maxs.append(float(line[2]) if isfloat(line[2]) else None)
    mins.append(float(line[3]) if isfloat(line[3]) else None)
    if isfloat(line[2]) and isfloat(line[3]):
        x.append([int(line[0]), m[line[1]]])
    else:
        testx.append([int(line[0]), m[line[1]]])
y = ([(x + y) / 2 for x, y in zip(maxs, mins) if x is not None and y is not None])
# x = [[int(line[0]), m[line[1]]] for i in range(n) if maxs[i] is not None and mins[i] is not None]
model = ensemble.GradientBoostingRegressor()
model.fit(x, y)
a = list(model.predict(testx))
print(x)
print(y)
print(testx)

for i in range(len(inputs)):
    if mins[i] == None:
        print(2 * a.pop(0) - maxs[i])
    if maxs[i] == None:
        print(2 * a.pop(0) - mins[i])

# plt.plot(x, y)
