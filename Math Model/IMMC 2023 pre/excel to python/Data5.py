import pandas as pd
import numpy
df = pd.read_excel("data.xlsx")
data = df.to_numpy()

def separate4(data, h): #done 
    #h = 107 99.1%
    if data[6]**4 * data[17] * data[21]**2 * data[24] * data[20] / (data[14]*1000000000) > h:
        sp = 4
    else:
        sp = 9
    return sp
   
def separate5(data, h): #done 
    #h = 14 100% accuracy
    if data[7] + data[25] / 10 <= h:
    
        sp = 5 
    else:
        sp = 9
    return sp
    
def separate8x45(data, h): #done 
    #h = 524 15-427 98.9%
    if data[16]*data[17]*data[24]*data[21]*data[22]/(data[20]*data[20]*100) > h:
        sp = 8
    else:
        sp = 9
    
    return sp
    
def separate1x458(data, h): #done
    #h = 298 56-357 98.4% 
    if data[3] * data[8]**2 * data[12] * data[18] * data[25] * data[7] * data[9] * data[16] / 1000000000 > h:
        sp = 1
    else:
        sp = 9
    
    return sp
    
def diff2and3(data, h): #done 
    # h = 103 100% 
    if data[3]*data[5]*data[7]*data[14]/(data[20]*data[24]*data[13]) > h:
        sp = 2
    else:
        sp = 3
    return sp

def diff6and7(data, h): #done 
    # h = 431 100% 
    if data[3] * data[10] > h: 
        sp = 7 
    else: 
        sp = 6
    return sp

def diff23and67x4518(data, h): 
    #h = -19 97.5%
    if data[8]  - data[4] * 2 + data[10] + data[13] + data[15] > h:
        sp = 23
    else:
        sp = 67
    return sp


def Orange_Sex(data, h): #done hard to improve
    if 2*data[18] + data[19] + 2*data[21] + data[22] + data[23] + data[24] + data[25] - data[16] - data[17] - 3 * data[4] + data[10] > h:
    #h = -26 94.3%
        sex = 1
    else:
        sex = 2
    return sex

def deff_sp_sex(lizard): 
    gender = Orange_Sex(lizard, -26)
    
    if separate5(lizard, 14) == 5:
        species = 5
    
    elif separate4(lizard, 107) == 4:
        species = 4
    
    elif separate8x45(lizard, 524) == 8:
        species = 8
    
    elif separate1x458(lizard, 298) == 1:
        species = 1
    
    elif diff23and67x4518(lizard, -19) == 23:
        if diff2and3(lizard, 103) == 2:
            species = 2
            
        else:
            species = 3
    elif diff23and67x4518(lizard, 311) == 67:
        if diff6and7(lizard, 431) == 6:
            species = 6
            
        else:
            species = 7
    
    final = f"Species: {species}, Gender: {gender}"
    deff = [species, gender, final]
    return deff

#main function: tell species and gender

right_sp = 0
right_sex = 0
right_all = 0
incorrect = 0

for i in range(564):
    lizard = list(data[i])
    result = deff_sp_sex(lizard)
    if lizard[0] == result[0] and lizard[1] == result[1]:
        right_all += 1
    elif lizard[0] == result[0] and lizard[1] != result[1]:
        right_sp += 1
    elif lizard[1] == result[1] and lizard[0] != result[0]:
        right_sex += 1
    else:
        incorrect += 1
    
    

print(f"All correct: {right_all}; Right species only: {right_sp}; Right sex only: {right_sex}")
print(f"Incorrect: {incorrect}")
