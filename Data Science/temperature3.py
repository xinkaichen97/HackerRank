import numpy as np
from sklearn import ensemble
from datetime import date, timedelta


train = [34.38, 34.36, 34.74, 35.26, 35.23, 35.29, 35.64, 36.02, 36.1, 36.98, 37.01, 36.75, 36.01, 35.66, 34.72, 33.9,
         32.62, 31.51, 30.73, 29.5, 26.94, 25.47, 23.84, 22.55]
test = [36.02, 36.1, 36.98, 37.01, 36.75, 36.01, 35.66, 34.72, 33.9, 32.62, 31.51, 30.73, 29.5, 26.94, 25.47, 23.84,
        22.55, 21.03, 19.92, 18.77, 18.48, 18.07, 17.91, 17.11]
startDate = '2013-01-01'
endDate = '2013-01-01'
p = 1
n = 1


def predictTemperature(startDate, endDate, temperature, n):
    p = int(len(temperature) / 24)
    x = []
    for i in range(1, ((24 * p) + 1)):
        x.append(i)
    x = np.asarray(x).reshape(-1, 1)
    print(x)
    y = np.array(temperature)
    model = training(x, y)
    f = x[-1] + 1
    z = []
    for i in range(24 * n):
        z.append(f)
        f += 1
    print(testing(z, model))
    """# Data Cleaning
    # get all dates from start date to end date
    x, delta = get_dates(startDate, endDate)
    X = []

    # Training Data -
    # create a X feature matrix - Year, Month, Date, Hour
    # delta(days)*24(hours) > total training values
    for i in x:
        temp = x[i].split('-')
        for i in range(0, 24):
            X.append(temp.append(i))
        X = np.array()
        # Y values  - Temperatures
        # delta(days)*24(hours)
        Y = np.array(temperature)

        # Model Building
        model = training(X, Y)

        # Model Evaluation
        # creatign X values before prediction
        X = get_dates(0, 0, n)
        # Model Testing
        result = Testing(X, model)"""


def get_dates(start=0, end=0, delta=0):
    d1 = date(start[:4], start[6:8], start[9:11])  # start date
    d2 = date(end[:4], end[6:8], end[9:11])  # end date
    delta = d2 - d1  # timedelta
    X = []
    for i in range(delta.days + 1):
        X.append(d1 + timedelta(days=i))
    return X, delta


def training(x, y):
    model = ensemble.GradientBoostingRegressor()
    model.fit(x, y)
    """print('Coefficient: \n', model.coef_)
    print('Intercept: \n', model.intercept_)
    coefs = zip(model.coef_, X.columns)
    #model.__dict__
    print("sl = %.1f + " % model.intercept_ + " + ".join("%.1f %s" % coef for coef in coefs))"""
    return model


def testing(x, model):
    return model.predict(x)


print(predictTemperature(startDate, endDate, train, n))
