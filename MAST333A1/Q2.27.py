import pandas as pd
import numpy as np
from scipy import stats
import os
import matplotlib.pyplot as plt

os.system('clear')

weight = [1.08, 1.06, 0.89, 0.89, 0.98, 1.14, 0.89, 0.98, 0.97, 1.38, 
          0.96, 1.14, 1.18, 0.75, 1.12, 0.92, 1.41, 0.96, 1.12, 1.18, 
          1.28, 1.08, 0.93, 1.17, 0.83, 0.87, 1.24]

weight.sort()

weightLen = len(weight)

def stem_and_leaf_plot(data):
    stems = {}
    for number in data:
        stem = int(number * 10) / 10
        leaf = int( (100 * ( number - stem)) // 1)
        if stem in stems:
            stems[stem].append(leaf)
        else:
            stems[stem] = [leaf]
    
    for stem, leaves in sorted(stems.items()):
        print(f"{stem} | {' '.join(str(leaf) for leaf in sorted(leaves))}")

stem_and_leaf_plot(weight)

mean_weight = np.mean(weight)
std_dev_weight = np.std(weight)

print(f"Mean: {mean_weight:.2f}")
print(f"Standard Deviation: {std_dev_weight:.2f}")

for i in range(1, 4):
    print(f"Mean + {i}Standard Deviation: [{mean_weight - i*std_dev_weight:.2f}m, {mean_weight + i*std_dev_weight:.2f}m]")