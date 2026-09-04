import matplotlib.pyplot as plt
import pandas as pd

f = open("Doc3.txt")

content = f.readlines()

num = len(content)
# print(content)

color = []

for i in range(24):
    color.append('g')
for i in range(6):
    color.append('lightgreen')
for i in range(2):
    color.append('pink')
for i in range(22):
    color.append('r')
for i in range(3):
    color.append('g')
for i in range(2):
    color.append('lightgreen')
for i in range(1):
    color.append('pink')
for i in range(14):
    color.append('black')
    
    
for i in range(len(content)):
    content[i] = content[i].split(" ")
    content[i] = [content[i][0], float(content[i][-1].strip("\n"))]

df = pd.DataFrame(content)

print(df)

plt.figure(figsize = [8, 10])
    
'''
for i in range(num):
    if df[1].loc[i] > 0.5 and color[i] == 'r':
        print(df[0].loc[i])

plt.plot([-1, 74], [0.5, 0.5], color = 'b')
plt.scatter(range(74), df[1], c = color)

plt.show()
'''

maybe_sport = []
maybe_value = []
maybe_color = []

for i in range(num):
    if color[i] == 'black':
        maybe_sport.append(df[0].loc[i])
        maybe_value.append(df[1].loc[i])
        if (df[1].loc[i] > 0.5):
            maybe_color.append('g')
        else:
            maybe_color.append('r')
    
plt.bar(maybe_sport, maybe_value, color = maybe_color)
plt.title("Prediction of Sports to be in or not in Olympics")
plt.xticks(rotation=45, ha='right')
plt.xlabel("sports in considerations")
plt.ylabel("rating")
plt.yticks([0, 0.5, 1])
plt.ylim([0, 1])

plt.savefig("Graph_predict")

