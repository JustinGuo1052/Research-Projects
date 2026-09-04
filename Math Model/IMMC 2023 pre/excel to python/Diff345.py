import pandas as pd
import numpy
df = pd.read_excel("data.xlsx") 
data1 = df.to_numpy()

S33 = 0
S34 = 0
S35 = 0
S43 = 0
S44 = 0
S45 = 0
S53 = 0
S54 = 0
S55 = 0
for i in range(564):
    data = list(data1[i])
    if data[0] != 3 and data[0] != 4 and data[0] != 5:
        continue
    if data[7] <= 11: 
        sp = 5
    elif data[6] < 26.1:     
        sp = 3
    else:
        sp = 4
    if data[0] == 3 and sp == 3:
        S33 += 1
        
    elif data[0] == 3 and sp == 4:
        S34 += 1
    elif data[0] == 3 and sp == 5:
        S35 += 1    
    elif data[0] == 4 and sp == 4:
        S44 += 1   
    elif data[0] == 4 and sp == 5:
        S45 += 1    
    elif data[0] == 4 and sp == 3:
        S43 += 1   
    elif data[0] == 5 and sp == 5:
        S55 += 1    
    elif data[0] == 5 and sp == 3:
        S53 += 1    
    elif data[0] == 5 and sp == 4:
        S54 += 1

print(f"Correct 3 Classfied 3: {S33}")
print(f"Correct 3 Classfied 4: {S34}")
print(f"Correct 3 Classfied 5: {S35}")
print(f"Correct 4 Classfied 4: {S44}")
print(f"Correct 4 Classfied 5: {S45}")
print(f"Correct 4 Classfied 3: {S43}")
print(f"Correct 5 Classfied 5: {S55}")
print(f"Correct 5 Classfied 3: {S53}")
print(f"Correct 5 Classfied 4: {S54}")

