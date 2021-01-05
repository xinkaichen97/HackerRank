import numpy as np
import pandas as pd
import csv
import itertools
import math
from apyori import apriori

def attributesSet(numberOfAttributes, supportThreshold):
    # Write your code here
    attributes = ['age', 'sex', 'education', 'native-country', 'race', 'marital-status', 'workclass', 'occupation', 'hours-per-week', 'income', 'capital-gain', 'capital-loss']
    combo = []
    fin = []
    for c in itertools.combinations(attributes, numberOfAttributes):
        #print(c)
        combo.append(list(c))
    # data_url = 'https://s3.amazonaws.com/istreet-questions-us-east-1/443605/census.csv'
    data_frame = pd.read_csv('census.csv')
    data_frame.columns = attributes
    total = len(data_frame.index)
    print(total)
    ceiling = math.ceil(supportThreshold * total)
    for i in combo:
        print(i)
        group = data_frame.groupby(i).size().sort_values(ascending=False)
        groups = group[group > ceiling].index
        satisfied = list(groups)
        for j in satisfied:
            fin.append(','.join(j))
    for item in fin:
        print(item)
    return fin


def attributesSet2(numberOfAttributes, supportThreshold):
    census_data = pd.read_csv('census.csv', header=None)
    num_records = len(census_data)
    print(num_records)
    records = []
    for i in range(0, num_records):
        records.append([str(census_data.values[i, j]) for j in range(0, 12)])
    print(records[0])
    association_rules = apriori(records, min_support=supportThreshold, min_confidence=0.2, min_lift=1, min_length=numberOfAttributes, max_length=numberOfAttributes)
    association_results = list(association_rules)
    #print(association_results)
    for item in association_results:
        pair = item[0]
        items = [x for x in pair]
        if len(items) == 4:
            print(','.join(items))


attributesSet(4, 0.6)
#attributesSet2(4, 0.6)
