import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as mlt
from apyori import apriori


def read_data(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        headers = reader.fieldnames
        census = []
        census_dict = {}
        for header in headers:
            census_dict[header] = None
        print(headers)
        for line in reader:
            for header in headers:
                if line[header] != '0':
                    census_dict[header] = line[header]
                else:
                    census_dict[header] = 'None'
            census.append(census_dict)
            census_dict = {}
    return census


def toString(dic):
    dic_str = ''
    for key in dic.keys():
        dic_str += (key + '=' + dic[key] + ',')
    dic_str = dic_str[:-1]
    return dic_str


def arrangingRules(rules):
    x_list, xy_list = [], []
    for rule in rules:
        x = rule.split('}=>{')[0][1:].split(',')
        y = rule.split('}=>{')[1][:-1].split(',')
        x_list.append(x)
        xy_list.append(x + y)
    print(x_list, xy_list)
    census_data = pd.read_csv('census.csv', header=None)
    num_records = len(census_data)
    print(num_records)
    records = []
    for i in range(0, num_records):
        records.append([str(census_data.values[i, j]) for j in range(0, 12)])
    print(records)
    association_rules = apriori(records, min_support=0.3, min_confidence=0.2, min_lift=1, min_length=3, max_length=3)
    association_results = list(association_rules)
    print(len(association_results))
    results = []
    for item in association_results:
        print(item)
    for item in association_results:
        pair = item[0]
        items = [x for x in pair]
        value0 = ",".join(items)
        value2 = str(item[1])  # to convert into object
        rows = (value0, value2)
        results.append(rows)
    labels = ['Attribute', 'Support']
    census = pd.DataFrame.from_records(results, columns=labels)
    x_support, xy_support = [], []
    for j in range(len(x_list)):
        for i in range(len(census)):
            element = census['Attribute'][i]
            if len(element) == sum([len(item) for item in x_list[j]]) + len(x_list[j]) - 1:
                match = True
                for rule in x_list[j]:
                    if rule not in element:
                        match = False
                if match:
                    x_support.append(census['Support'][i])
            if len(element) == sum([len(item) for item in xy_list[j]]) + len(xy_list[j]) - 1:
                match = True
                for rule in xy_list[j]:
                    if rule not in element:
                        match = False
                if match:
                    xy_support.append(census['Support'][i])
    print(x_support, xy_support)
    confidences = [float(xy) / float(x) for x, xy in zip(x_support, xy_support)]
    print(confidences)
    result = list(zip(rules, confidences))
    print(result)
    result = sorted(result, key=lambda x: x[1], reverse=True)
    for rule, confid in result:
        print(rule)


def arrangingRules2(rules):
    x_list, xy_list = [], []
    for rule in rules:
        x = rule.split('}=>{')[0][1:].split(',')
        y = rule.split('}=>{')[1][:-1].split(',')
        x_list.append(x)
        xy_list.append(x + y)
    census_data = pd.read_csv('census.csv', header=None)
    num_records = len(census_data)
    records = []
    for i in range(0, num_records):
        records.append([str(census_data.values[i, j]) for j in range(0, 12)])
    x_support, xy_support = [], []
    for j in range(len(x_list)):
        x_count = 0
        xy_count = 0
        for i in range(len(records)):
            match = True
            for rule in x_list[j]:
                if rule not in records[i]:
                    match = False
            if match:
                x_count += 1
            match = True
            for rule in xy_list[j]:
                if rule not in records[i]:
                    match = False
            if match:
                xy_count += 1
        x_support.append(x_count / 30162)
        xy_support.append(xy_count / 30162)
    confidences = [float(xy) / float(x) for x, xy in zip(x_support, xy_support)]
    result = list(zip(rules, confidences))
    result = sorted(result, key=lambda x: x[1], reverse=True)
    rules = []
    for rule, confid in result:
        rules.append(rule)
    return rules


if __name__ == '__main__':
    rules = ['{native-country=United-States,capital-gain=None}=>{capital-loss=None}',
             '{capital-gain=None,capital-loss=None}=>{native-country=United-States}',
             '{native-country=United-States,capital-loss=None}=>{capital-gain=None}']
    arrangingRules(rules)