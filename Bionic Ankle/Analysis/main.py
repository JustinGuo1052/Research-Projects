import matplotlib.pyplot as plt
import pandas as pd

angles = [-25, -20, -15, -10, -5, 0, +5, +10, +15, +20]
n = len(angles)

dfs = []
for i in range(n):
    dfs.append(pd.read_csv(f"{angles[i]}BIJ.tab", sep='\t', header=1))
    dfs[i].columns = ['time', 'force']
    dfs[i]['time'] = dfs[i]["time"] * 100000 / 5


peak = {}

for i in range(n):
    peak[angles[i]] = (dfs[i]['force'].max())

print(peak)

average = {}

normal = 50
for i in range(n):
    time_interval = dfs[i].loc[1, 'time'] - dfs[i].loc[0, 'time']
    test = dfs[i].loc[dfs[i]['force'] > normal]
    average[angles[i]] = test['force'].sum() / len(test['force']) / (len(test['force']) * time_interval)

print(average)

plt.figure()
for i in range(n):
    plt.figure()
    plt.plot(dfs[i]['time'], dfs[i]['force'], label=angles[i])
    plt.savefig(f"{angles[i]}_graph.png")
plt.figure()

for i in range(n):
    plt.plot(dfs[i]['time'], dfs[i]['force'], label=angles[i])
plt.xlabel("Time")
plt.ylabel("Force")
plt.xlim([0, 5000])
plt.legend(title="Angle")
plt.savefig(f"all_compare.png")

plt.figure()
plt.bar(peak.keys(), peak.values())
plt.savefig("Peak.png")

plt.figure()
plt.bar(average.keys(), average.values())
plt.savefig("Average.png")




