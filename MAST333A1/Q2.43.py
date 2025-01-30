import pandas as pd
import numpy as np
from scipy import stats
import os


os.system('clear')

data = np.array([8, 7, 1, 4, 6, 6, 4, 5, 7, 6, 3, 0])
data.sort()

dataLen = len(data)

min = data[0]
max = data[dataLen - 1]

q1 = np.percentile(data, 25, interpolation='linear')
q3 = np.percentile(data, 75, interpolation='linear')

median = np.median(data)

mean = np.mean(data)
stdDev = round(np.std(data, ddof=1), 2)

zScore = stats.zscore(data, axis=None)

roundedZScore = [round(num, 2) for num in zScore]

print(f'''
5 Number Summary
      Min: {min}, Q1: {q1}, Median: {median}, Q3: {q3}, Max: {max}''')

print(f'''
Measures of Variability
      Mean: {mean}
      Standard Deviation: {stdDev}
      ''')


dataSet = {'Data': data, 'Z Score' : roundedZScore}

df = pd.DataFrame(dataSet)

print(df)

