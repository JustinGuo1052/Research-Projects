import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gauseian_

df = pd.read_excel("N_Sports.xlsx")

print(df)

color = []

num_sports = len(df)


for i in range(num_sports):
    if (df["Label"].loc[i] == 1):
        color.append('g')
    elif (df["Label"].loc[i] == 0):
        color.append('r')
    else:
        color.append('black')





for a in range(1, len(df.columns) - 1):
    '''
    print(df[df.columns[i]])
    plt.figure()
    plt.legend({'green': "Olympics", "red": "Non in Olympics", "black": "undecided"})
    plt.ylim([0, 1.1])
    plt.scatter(range(num_sports), df[df.columns[i]], c = color)
    plt.savefig("N_" + df.columns[i])
    '''

    plt.figure()
    o, i = np.histogram(df.loc[df["Label"] == 0, df.columns[a]], bins = 100)
    no, j = np.histogram(df.loc[df["Label"] == 1, df.columns[a]], bins = 100)
    box = np.ones(100) / 100
    o_= np.convolve(o, box, mode = "same")
    no_= np.convolve(no, box, mode = "same")
    plt.plot(i[:-1], o_, color = 'g')
    plt.plot(j[:-1], no_, color = 'r')
    
    plt.title("N_" + df.columns[a])

    plt.savefig("H_N_" + df.columns[a])
    



        

