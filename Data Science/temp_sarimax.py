import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
#from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
#from statsmodels.tsa.seasonal import seasonal_decompose
from pmdarima import auto_arima
#from sklearn.metrics import mean_squared_error
#from statsmodels.tools.eval_measures import rmse
from datetime import date, timedelta

train = [34.38, 34.36, 34.74, 35.26, 35.23, 35.29, 35.64, 36.02, 36.1, 36.98, 37.01, 36.75, 36.01, 35.66, 34.72, 33.9,
         32.62, 31.51, 30.73, 29.5, 26.94, 25.47, 23.84, 22.55, 34.38, 34.36, 34.74, 35.26, 35.23, 35.29, 35.64, 36.02,
         36.1, 36.98, 37.01, 36.75, 36.01, 35.66, 34.72, 33.9,
         32.62, 31.51, 30.73, 29.5, 26.94, 25.47, 23.84, 22.55]
startDate = '2013-01-01'
endDate = '2013-01-02'
p = 1
n = 2


def predictTemperature(startDate, endDate, temperature, n):
    stdate_split = startDate.split('-')
    enddate_split = endDate.split('-')
    stdate = date(int(stdate_split[0]), int(stdate_split[1]), int(stdate_split[2]))
    enddate = date(int(enddate_split[0]), int(enddate_split[1]), int(enddate_split[2]))
    delta = enddate - stdate
    print(delta)
    days = []
    for i in range(delta.days + 1):
        day = stdate + timedelta(days=i)
        print(str(day))
        days.append(str(day))
    print(days)
    hours = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
             '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    obs = [x + ' ' + y for x in days for y in hours]
    print(obs)
    """x = ['2013-01-01 00:00', '2013-01-01 01:00', '2013-01-01 02:00', '2013-01-01 03:00', '2013-01-01 04:00',
         '2013-01-01 05:00', '2013-01-01 06:00', '2013-01-01 07:00', '2013-01-01 08:00', '2013-01-01 09:00',
         '2013-01-01 10:00', '2013-01-01 11:00', '2013-01-01 12:00', '2013-01-01 13:00', '2013-01-01 14:00',
         '2013-01-01 15:00', '2013-01-01 16:00', '2013-01-01 17:00', '2013-01-01 18:00', '2013-01-01 19:00',
         '2013-01-01 20:00', '2013-01-01 21:00', '2013-01-01 22:00', '2013-01-01 23:00', '2013-01-02 00:00',
         '2013-01-02 01:00', '2013-01-02 02:00', '2013-01-02 03:00', '2013-01-02 04:00',
         '2013-01-02 05:00', '2013-01-02 06:00', '2013-01-02 07:00', '2013-01-02 08:00', '2013-01-02 09:00',
         '2013-01-02 10:00', '2013-01-02 11:00', '2013-01-02 12:00', '2013-01-02 13:00', '2013-01-02 14:00',
         '2013-01-02 15:00', '2013-01-02 16:00', '2013-01-02 17:00', '2013-01-02 18:00', '2013-01-02 19:00',
         '2013-01-02 20:00', '2013-01-02 21:00', '2013-01-02 22:00', '2013-01-02 23:00']"""
    y = temperature
    df = pd.DataFrame({'Hour': obs, 'Temp': y})
    df.Hour = pd.to_datetime(df.Hour)
    df = df.set_index('Hour')
    print(df.to_string())
    # a = seasonal_decompose(df, model="add")
    # a.plot()
    #param = auto_arima(df['Temp'], seasonal=True, m=12, max_p=3, max_d=3, max_q=3, max_P=4, max_D=4, max_Q=4)
    #print(param.ord)
    arima_model = SARIMAX(df['Temp'], order=(1, 0, 0), seasonal_order=(3, 0, 0, 12), initialization='approximate_diffuse')
    arima_result = arima_model.fit()
    arima_result.summary()
    arima_pred = arima_result.predict(start=len(df), end=len(df) + n * 24 - 1, typ="levels").rename("ARIMA Predictions")
    print(arima_pred)
    pred = [line for line in arima_pred]
    return pred



"""for i in range(24):
    if i < 10:
        print('\'0' + str(i) + ':00\'', end=',')
    else:
        print('\'' + str(i) + ':00\'', end=',')"""
print(predictTemperature(startDate, endDate, train, n))
