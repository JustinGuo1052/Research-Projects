import matplotlib.pyplot as plt
import pandas as pd

f1 = open("Doc1.txt")
f2 = open("Doc3.txt")

c1 = f1.readlines()
c2 = f2.readlines()

print(c2)
content = []


for i in range(len(c1)):
    c1[i] = c1[i].split(" ")
    c1[i] = [c1[i][0], float(c1[i][-1].strip("\n"))]
    c2[i] = c2[i].split(" ")
    c2[i] = [c2[i][0], float(c2[i][-1].strip("\n"))]
    print(c1[i], c2[i])
    content.append([c1[i][0], c1[i][1] - c2[i][1]])

df = pd.DataFrame(content)

print(df)

plt.figure()
plt.scatter(range(74), df[1])
plt.show()
    
    

