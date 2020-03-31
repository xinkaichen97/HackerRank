#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calcMissing' function below.
#
# The function accepts STRING_ARRAY readings as parameter.
#
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor


def calcMissing(readings):
    timestamps = [line.split('\t')[0] for line in readings]
    values = [line.split('\t')[1] for line in readings]
    #print(timestamps)
    #print(values)
    df = pd.DataFrame({'Time': timestamps, 'Value': values})
    missing_df = df[df['Value'].str.contains('Missing')]
    missing_df = missing_df.loc[:, missing_df.columns != 'Value']
    train_df = pd.merge(df, missing_df, indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1)
    train_df.Time = pd.to_datetime(train_df.Time)
    #train_df = train_df.set_index('Time')
    train_df = train_df.reset_index(drop=True)
    missing_df.Time = pd.to_datetime(missing_df.Time)
    #missing_df = missing_df.set_index('Time')
    """arima_model = SARIMAX(train_df['Value'], order=(1, 0, 0), seasonal_order=(3, 0, 0, 12), initialization='approximate_diffuse')
    arima_result = arima_model.fit()
    arima_pred = arima_result.predict(start=0, end=len(df) + n * 24 - 1, typ="levels").rename("ARIMA Predictions")"""
    clf = GradientBoostingRegressor(n_estimators=100, learning_rate=0.5, max_depth=2)
    clf.fit(train_df.loc[:, train_df.columns == 'Time'], train_df.loc[:, train_df.columns == 'Value'])
    predictions = []
    for i, j in enumerate(clf.predict(missing_df)):
        print(j)


if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = input()
        readings.append(readings_item)

    calcMissing(readings)