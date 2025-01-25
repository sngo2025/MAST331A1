import pandas as pd
import numpy as np

data = [8, 7, 1, 4, 6, 6, 4, 5, 7, 6, 3, 0]
data.sort()

dataSet = {'Data': data}

df = pd.DataFrame(dataSet)

print(df)