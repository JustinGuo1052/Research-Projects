import pandas as pd
import numpy
df = pd.read_excel("data.xlsx")
data = df.to_numpy()

def diff23and67x4518(data, h): 
    #h = 311 95.0%
    if data[8]  - data[4] * 2 + data[10] + data[13] + data[15] > h:
        sp = 23
    else:
        sp = 67
    return sp


right1 = 0
right9 = 0
wrong1 = 0
wrong9 = 0
    
#Code to find the highest percentage by looping through h
percent = {}
for j in range(-100, 1000):    
    for i in range(564):
        lizard = list(data[i])
        if lizard[0] == 1 or lizard[0] == 4 or lizard[0] == 5 or lizard[0] == 8:
            continue
        s = diff23and67x4518(lizard, j)
        
        if (lizard[0] == 2 or lizard[0] == 3) and s == 23:
            right1 += 1
        elif (lizard[0] == 6 or lizard[0] == 7) and s == 67:
            right9 += 1
        elif (lizard[0] == 2 or lizard[0] == 3) and s == 67:
            wrong1 += 1
        elif (lizard[0] == 6 or lizard[0] == 7) and s == 23:
            wrong9 += 1
    percent[j] = (right1 + right9)/(right1 + right9 + wrong1 + wrong9)
    right1 = 0
    right9 = 0
    wrong1 = 0
    wrong9 = 0

max_num = 0

for i in percent.items():
    if max_num < i[1]:
        max_num = i[1]
        key = i[0]
print(key, max_num)
