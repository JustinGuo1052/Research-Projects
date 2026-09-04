import pandas as pd
import numpy
df = pd.read_excel("data.xlsx")
data = df.to_numpy()

# Problem 1 differentiates species 5 from others using FPNr
# Problem 2 differentiates species 5 from others using 1 morphometric and pholidosis characteristic

right5 = 0 #variable: number of correct species 5
righto = 0 #variable: number of correct species others
wrong5 = 0 #variable: number of incorrect species 5(real species_num)
wrongo = 0 #variable: number of incorrect species others(real species_num)

def FPNr_Sp5(data): #Problem 1 Used
    if data[7] <= 11: #function(FPNr) = FPNr <= 11
        sp = 5 #if f(FPNr) <= h, then species_num is probably 5
    else:
        sp = 'o' #elsewise other species
    
    #Code to help control the variables
    if data[0] == 5 and sp == 5:
        return 1
    elif data[0] != 5 and sp == 'o':
        return 2
    elif data[0] == 5 and sp == 'o':
        return 3
    elif data[0] != 5 and sp == 5:
        return 4

#all else defined functions are simliar to the first defined function
def FPNrandHFL_Sp5(data, h): #Problem 2 Used
    if data[7] + data[25]/10 <= h: #function(FPNr, HFL) = FPNr + HFL/10 < h
        #h = 14 100%
        sp = 5 
    else:
        sp = 9
    return sp

right1 = 0
right9 = 0
wrong1 = 0
wrong9 = 0
    
#Code to find the highest percentage by looping through h
'''
percent = {}
for j in range(0, 1000):    
    for i in range(564):
        lizard = list(data[i])
        s = FPNrandHFL_Sp5(lizard, j)
        if lizard[0] == 5 and s == 5:
            right1 += 1
        elif lizard[0] != 5 and s == 9:
            right9 += 1
        elif lizard[0] == 5 and s == 9:
            wrong1 += 1
        elif lizard[0] != 5 and s == 5:
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
'''
'''
for i in range(564):
        lizard = list(data[i])
        s = FPNrandHFL_Sp5(lizard, 14)
        if lizard[0] == 5 and s == 5:
            right1 += 1
        elif lizard[0] != 5 and s == 9:
            right9 += 1
        elif lizard[0] == 5 and s == 9:
            wrong1 += 1
        elif lizard[0] != 5 and s == 5:
            wrong9 += 1


print(f"Correct identifed species 5: {right1}")
print(f"Correct identifed other species: {right9}")
print(f"Wrongly identifed species 5: {wrong1}")
print(f"Wrongly identifed other species: {wrong9}")
'''


#Problem 3 differentiates gender

rightM = 0 #variable: number of correct male
rightF = 0 #variable: number of correct female
wrongM = 0 #variable: number of incorrect male(real gender)
wrongF = 0 #variable: number of incorrect female(real gender)

def Orange_Sex(data, h): #Problem 3 Used 
    if 2*data[18] + data[19] + 2*data[21] + data[22] + data[23] + data[24] + data[25] - data[16] - data[17] - 3 * data[4] + data[10] > h:
        #function(VSN, SCGr, SVL, TRL, HL, PL, HW, HH, MO, FFL, HFL) = -VSN +SCGr -SVL -TRL +HL +PL +HW +HH +MO +FFL +HFL > h
        #Functions tried, and their best h value and accuracy
        #| 18 19 21 22 23 24 25 -16 -17 | h = 16 --> 85.6% 
        #| __ 19 21 22 23 24 25 -16 -17 | h = -3 --> 83.3%
        #| 18 __ 21 22 23 24 25 -16 -17 | h = 2 --> 84.2%
        #| 18 19 __ 22 23 24 25 -16 -17 | h = 8 --> 84.2%
        #| 18 19 21 __ 23 24 25 -16 -17 | h = 10 --> 85.1%
        #| 18 19 21 22 __ 24 25 -16 -17 | h = 6 --> 85.5%
        #| 18 19 21 22 23 __ 25 -16 -17 | h = -4 --> 84.8%
        #| 18 19 21 22 23 24 __ -16 -17 | h = -14 --> 81.2%
        #| 18 19 21 22 23 24 25 ___ -17 | h = 74 --> 74.8%
        #| 18 19 21 22 23 24 25 -16 ___ | h = 46 --> 82.3%
        #| 18 19 21 22 23 24 25 -16 -17 10 | h = 16 --> 87.8%
        #| 18 19 21 22 23 24 25 -16 -17 10 -4 | h = -1 --> 92.2%
        # Added 1 dec place | 18 19 21 22 23 24 25 -16 -17 10 -4 | h = -0.9 --> 92.6% 
        # Added 1 dec place | 18 19 21 22 23 24 25 -16 -17 10 -4 -4 | h = -26.7 --> 93.3%
        #New h = -26 94.3%
        sex = 1
    else:
        sex = 2
    if data[1] == 1 and sex == 1:
        return 11
    elif data[1] == 2 and sex == 2:
        return 22
    elif data[1] == 2 and sex == 1:
        return 21
    elif data[1] == 1 and sex == 2:
        return 12

def Smth_Sex(data, h): #Problem 3 Abandoned
    if data[21]/data[22] + data[16]/data[17] + (data[24] + data[25]) + (data[19]+data[23])/data[18] > h:
        #Head Width to Head Height (2) + Trunk Length to whole length(2) + Leg Length(19 + 31) + Head Length ratios(1)
        #h = 53.5 --> 67.2% success
        sex = 1
    else:
        sex = 2
    if data[1] == 1 and sex == 1:
        return 11
    elif data[1] == 2 and sex == 2:
        return 22
    elif data[1] == 2 and sex == 1:
        return 21
    elif data[1] == 1 and sex == 2:
        return 12
    
def Leg_Sex(data, h): #Problem 3 Abandoned
    if (data[24] + data[25]) > h:
        #Leg Length(19 + 31)
        # h = 47.9 -->66.1% success
        sex = 1
    else:
        sex = 2
    if data[1] == 1 and sex == 1:
        return 11
    elif data[1] == 2 and sex == 2:
        return 22
    elif data[1] == 2 and sex == 1:
        return 21
    elif data[1] == 1 and sex == 2:
        return 12

'''
#Code to find the highest percentage by looping through h
percent = {}
for j in range(-100, 300):    
    for i in range(564):
        lizard = list(data[i])
        result = Orange_Sex(lizard, j)
        if result == 11:
            rightM += 1
        elif result == 22:
            rightF += 1
        elif result == 12:
            wrongM += 1
        elif result == 21:
            wrongF += 1
    percent[j] = (rightM + rightF)/564
    rightM = 0
    rightF = 0
    wrongM = 0
    wrongF = 0

print(percent)
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
        result = Orange_Sex(lizard, -26)
        if result == 11:
            rightM += 1
        elif result == 22:
            rightF += 1
        elif result == 12:
            wrongM += 1
        elif result == 21:
            wrongF += 1
percent = (rightM + rightF)/564

print(f"Correct identifed male: {rightM}")
print(f"Correct identifed female: {rightF}")
print(f"Wrongly identifed male: {wrongM}")
print(f"Wrongly identifed female: {wrongF}")
print(f"correct percentage: {percent}")


