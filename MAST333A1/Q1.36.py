import pandas as pd
import numpy as np
from scipy import stats
import os
import matplotlib.pyplot as plt


os.system('clear')
 
hydroData = np.array([18200, 12600, 10000, 8730, 6400, 6300, 6000, 4500, 4200, 4200, 3840, 3444, 3300, 3100, 3000, 2940, 2715, 2700, 2541, 2512])
hydroData.sort()

hydroLen = len(hydroData)
min = hydroData[0]
max = hydroData[hydroLen - 1]


def stem_and_leaf_plot(data):
    stems = {}
    for number in data:
        stem = number // 1000
        leaf = number % 1000
        if stem in stems:
            stems[stem].append(leaf)
        else:
            stems[stem] = [leaf]
    
    for stem, leaves in sorted(stems.items()):
        print(f"{stem} | {' '.join(str(leaf).zfill(3) for leaf in sorted(leaves))}")

stem_and_leaf_plot(hydroData)