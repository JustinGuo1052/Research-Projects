import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("Sports.xlsx")

print(df)

color = []

num_sports = len(df)


for i in range(num_sports):
    if (df["MaleFemaleRatio"].iloc[i] == 0):
        continue
    print(df["MaleFemaleRatio"].iloc[i])
    a, b = df["MaleFemaleRatio"].iloc[i].split(":")
    a = float(a)
    b = float(b)
    df.at[i, "MaleFemaleRatio"] = a / b
    # df.replace(df["MaleFemaleRatio"].iloc[i], a / b)



for i in range(num_sports):
    if (df["Label"].loc[i] == 1):
        color.append('g')
    elif (df["Label"].loc[i] == 0):
        color.append('r')
    else:
        color.append('black')

for i in range(4, len(df.columns) - 1):
    print(df[df.columns[i]])
    plt.figure()
    plt.scatter(range(num_sports), df[df.columns[i]], c = color)
    plt.savefig(df.columns[i])
    
        

