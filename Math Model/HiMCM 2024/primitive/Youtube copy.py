import pandas as pd
import matplotlib.pyplot as plt
import math


df = pd.read_excel("Sports(2).xlsx", "Sheet3")
print(df)


index = "Min_E"
times = "1"
color = []
for i in range(34):
    color.append('g')
for i in range(26):
    color.append('r')
for i in range(14):
    color.append('black')
# Instagram
# Twitter
# Youtube
        
# print(result)

result = df[index]


plt.figure()
plt.title(index)
plt.ylim([0, 1000])
plt.scatter(list(range(74)), result, c = color)
plt.savefig(index + times)
