import matplotlib.pyplot as plt
import pandas as pd

angles = [-25, -20, -19, -15, -10, -5, 0, +5, +10, +15, +20]
n = len(angles)

dfs = []
for i in range(n):
    dfs.append(pd.read_csv(f"{angles[i]}BIJ.tab", sep='\t', header=1))
    dfs[i].columns = ['time', 'force']
    dfs[i]['time'] = dfs[i]["time"] * 100000 / 5