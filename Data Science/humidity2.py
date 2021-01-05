import pandas as pd
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot as plt

startDate = "2013-01-01"
endDate = "2013-01-01"
knownTimestamps = ['2013-01-01 00:00','2013-01-01 01:00','2013-01-01 02:00','2013-01-01 03:00','2013-01-01 04:00',
               '2013-01-01 05:00','2013-01-01 06:00','2013-01-01 08:00','2013-01-01 10:00','2013-01-01 11:00',
               '2013-01-01 12:00','2013-01-01 13:00','2013-01-01 16:00','2013-01-01 17:00','2013-01-01 18:00',
               '2013-01-01 19:00','2013-01-01 20:00','2013-01-01 21:00','2013-01-01 23:00']
humidity = ['0.62','0.64','0.62','0.63','0.63','0.64','0.63','0.64','0.48','0.46','0.45','0.44','0.46','0.47','0.48','0.49','0.51','0.52','0.52']
timestamps = ['2013-01-01 07:00','2013-01-01 09:00','2013-01-01 14:00','2013-01-01 15:00','2013-01-01 22:00']
# correct pred: 0.64, 0.55, 0.44, 0.44, 0.52


def predictMissingHumidity(startDate, endDate, knownTimestamps, humidity, timestamps):
    pred = []
    dataInput = pd.DataFrame({'knownTimestamps': knownTimestamps,'humidity': humidity})
    training = [float(x) for x in dataInput.humidity]
    #autocorrelation_plot(training)
    #plt.plot(knownTimestamps, training)
    #plt.show()
    for t in range(len(timestamps)):
        print(t)
        modelArima = ARIMA(training, order=(2, 2, 0))
        predict = modelArima.fit()
        #print(predict)
        humidityPred = float(predict.forecast()[0])
        pred.append(humidityPred)
        obs = timestamps[t]
    return pred



print(predictMissingHumidity(startDate, endDate, knownTimestamps, humidity, timestamps))
