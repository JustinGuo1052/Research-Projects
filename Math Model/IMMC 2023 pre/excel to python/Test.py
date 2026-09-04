import pandas as pd
import numpy
df = pd.read_excel("data.xlsx")
data = df.to_numpy()

rightM = 0 #variable: number of correct male
rightF = 0 #variable: number of correct female
wrongM = 0 #variable: number of incorrect male(real gender)
wrongF = 0 #variable: number of incorrect female(real gender)

def Orange_Sex(data, h): #Problem 3 Used 
    if 2 * data[18] + data[19] + 2 * data[21] + data[22] + data[23] + data[24] + data[25] - data[16] - data[17] - 3 * data[4] + data[10] > h:
        #function(VSN, SCGr, SVL, TRL, HL, PL, HW, HH, MO, FFL, HFL) = 2*-VSN + SCGr -SVL -TRL +2*HL +PL +2*HW +HH +MO +FFL +HFL > h 
        #Functions tried, and their best h value and accuracy
        # 18 19 21 22 23 24 25 -16 -17 10 -4 | h = -0.9 --> 92.6% 
        # 18 19 21 22 23 24 25 -16 -17 10 -4 -4 | h = -26.7 --> 93.3%?
        # 18 18 19 21 22 23 24 25 -16 -17 10 -4 -4 | h = -2 --> 94.1%
        # 18 18 19 21 22 23 24 25 -16 -17 10 -4 -4 -4 | h = -26 --> 94.3%
        sex = 1
    else:
        sex = 2
    return sex
'''
#Code to find the highest percentage by looping through h
percent = {}
for j in range(-200, 100):    
    for i in range(564):
        lizard = list(data[i])
        s = Orange_Sex(lizard, j)
        if lizard[1] == 1 and s == 1:
            rightM += 1
        elif lizard[1] == 2 and s == 2:
            rightF += 1
        elif lizard[1] == 1 and s == 2:
            wrongM += 1
        elif lizard[1] == 2 and 2 == 1:
            wrongF += 1
    percent[j] = (rightM + rightF)/564
    rightM = 0
    rightF = 0
    wrongM = 0
    wrongF = 0


max_num = 0

for i in percent.items():
    if max_num < i[1]:
        max_num = i[1]
        key = i[0]
print(key, max_num)

'''
#Code to show variables when h is given
for i in range(564):
        lizard = list(data[i])
        s = Orange_Sex(lizard, -26)
        if lizard[1] == 1 and s == 1:
            rightM += 1
        elif lizard[1] == 2 and s == 2:
            rightF += 1
        elif lizard[1] == 1 and s == 2:
            wrongM += 1
        elif lizard[1] == 2 and s == 1:
            wrongF += 1
percent = (rightM + rightF)/564

print(f"Correct identifed male: {rightM}")
print(f"Correct identifed female: {rightF}")
print(f"Wrongly identifed male: {wrongM}")
print(f"Wrongly identifed female: {wrongF}")
print(f"correct percentage: {percent}")

