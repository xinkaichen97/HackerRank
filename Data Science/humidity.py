import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor


# utility function
def predictMissingHumidity(startDate, endDate, knownTimestamps, humidity, timestamps):
    x = [int(abs((datetime.datetime.utcfromtimestamp(0) - datetime.datetime.strptime(item,"%Y-%m-%d %H:%M")).total_seconds())) for item in knownTimestamps]
    y = humidity

    lm = LinearRegression()
    lm.fit(np.array(x).reshape(-1,1),y)

    z = [int(abs((datetime.datetime.utcfromtimestamp(0) - datetime.datetime.strptime(item,"%Y-%m-%d %H:%M")).total_seconds())) for item in timestamps]
    return lm.predict(np.array(z).reshape(-1,1))

# dummy inputs
startDate = "2013-01-01"
endDate = "2013-01-01"
knownTimestamps = ['2013-01-01 00:00','2013-01-01 01:00','2013-01-01 02:00','2013-01-01 03:00','2013-01-01 04:00',
               '2013-01-01 05:00','2013-01-01 06:00','2013-01-01 08:00','2013-01-01 10:00','2013-01-01 11:00',
               '2013-01-01 12:00','2013-01-01 13:00','2013-01-01 16:00','2013-01-01 17:00','2013-01-01 18:00',
               '2013-01-01 19:00','2013-01-01 20:00','2013-01-01 21:00','2013-01-01 23:00']
humidity = ['0.62','0.64','0.62','0.63','0.63','0.64','0.63','0.64','0.48','0.46','0.45','0.44','0.46','0.47','0.48','0.49','0.51','0.52','0.52']
timestamps = ['2013-01-01 07:00','2013-01-01 09:00','2013-01-01 14:00','2013-01-01 15:00','2013-01-01 22:00']

# call the utility function
answer = predictMissingHumidity(startDate, endDate, knownTimestamps, humidity, timestamps)
print(answer)
