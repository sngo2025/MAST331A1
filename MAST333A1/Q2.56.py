import pandas as pd
import numpy as np
from scipy import stats
import os

os.system('clear')

fuelPrices = {
    "Edmonton": 89.227,
    "Calgary": 91.818,
    "London": 104.933,
    "Hamilton": 103.921,
    "Toronto": 105.057,
    "Montreal": 115.457,
    "Winnipeg": 90.560,
    "Halifax": 108.800,
    "Regina": 93.262,
    "Saskatoon": 96.673,
    "Quebec City": 119.458,
    "Vancouver": 121.273,
    "Victoria": 117.824
}

length = len(fuelPrices)
print(length)

sFuelPrices = dict(sorted(fuelPrices.items(), key=lambda item: item[1]))


df = pd.DataFrame(list(sFuelPrices.items()), columns=['City', 'Price'])
print(df, "\n")
