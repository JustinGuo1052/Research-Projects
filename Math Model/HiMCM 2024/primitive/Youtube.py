import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_excel("Sports.xlsx")
# print(df)

color = []
index = "Followers on Twitter"
users = 335700000
index2 = "Youtube's Most Views (Has to feature professional play, and is not a short)"
# Instagram
# Twitter
# Youtube
for i in range(23):
    color.append('g')
for i in range(1):
    color.append('r')
for i in range(3):
    color.append('g')
for i in range(1):
    color.append('r')
for i in range(4):
    color.append('g')
for i in range(15):
    color.append('r')




for i in range(47):
    df[index]= df[index].replace([df[index].loc[i]], math.sin(df[index].loc[i] * 2 * math.pi / users))
# print(result)
result = df[index]
plt.figure()
plt.title(index)
plt.ylim(0, 1)
plt.scatter(list(range(47)), result, c = color)
plt.savefig(index)
