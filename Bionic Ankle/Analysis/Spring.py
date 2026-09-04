import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

constants = [3, 4, 5, 6, 7, 8, 9]

n = len(constants)

dfs = []
for i in range(n):
    dfs.append(pd.read_csv(f"SPR_{constants[i]}.tab", sep='\t', header=1))
    dfs[i].columns = ['time', 'force']

turn_point = []
max_point = []

integral = []

for i in range(n):
    sum = 0
    for j in range(len(dfs[i]) - 1):
        sum += dfs[i].iloc[j, 1] * (dfs[i].iloc[j + 1, 0] - dfs[i].iloc[j, 0])
    integral.append(sum)

plt.figure()
plt.bar(constants, integral)
plt.savefig("momentum.png")

'''
for i in range(n):
    index = -1
    max_index = -1
    for j in range(len(dfs[i])):
        if dfs[i].iloc[j, 1] > max_index:
            max_index = dfs[i].iloc[j, 1]
            index = j
    turn_point.append(index)
    max_point.append(max_index)




dfs_split_1 = []
dfs_split_2 = []

for i in range(n):
    dfs_split_1.append(dfs[i].iloc[:turn_point[i]])
    dfs_split_2.append(dfs[i].iloc[turn_point[i]:])

np_time_1 = []
np_force_1 = []
np_time_2 = []
np_force_2 = []

slope_1 = []
slope_2 = []

for i in range(n):
    np_time_1.append(np.array(dfs_split_1[i]["time"]))
    np_force_1.append(np.array(dfs_split_1[i]['force']))
    s1, i1 = np.polyfit(np_time_1[i], np_force_1[i], 1)
    slope_1.append(abs(s1))
    np_time_2.append(np.array(dfs_split_2[i]["time"]))
    np_force_2.append(np.array(dfs_split_2[i]['force']))
    s2, i2 = np.polyfit(np_time_2[i], np_force_2[i], 1)
    slope_2.append(abs(s2))

plt.figure()
plt.bar(constants, slope_1)
plt.savefig("first_slopes.png")
plt.figure()
plt.bar(constants, slope_2)
plt.savefig("second_slopes.png")

plt.figure()
plt.bar(constants, max_point)
plt.savefig("max_spring.png")
'''

'''
plt.figure()
for i in range(n):
    plt.plot(dfs_split_1[i]['time'], dfs_split_1[i]['force'], label=constants[i])
plt.show()

plt.figure()
for i in range(n):
    plt.plot(dfs_split_2[i]['time'], dfs_split_2[i]['force'], label=constants[i])
plt.show()
'''


'''
plt.figure()
for i in range(n):
    plt.figure()
    plt.plot(dfs[i]['time'], dfs[i]['force'], label=constants[i])
    plt.savefig(f"Sc_{constants[i]}_graph.png")
plt.figure()

for i in range(n):
    plt.plot(dfs[i]['time'], dfs[i]['force'], label=constants[i])
plt.xlabel("Time")
plt.ylabel("Force")

plt.legend(title="Spring")
plt.savefig(f"all_s_compare.png")
'''