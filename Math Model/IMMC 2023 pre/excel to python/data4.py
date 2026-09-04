import pandas as pd
import numpy
df = pd.read_excel("data.xlsx") #read excel file to get data
data = df.to_numpy() #change data to array form for easier action

def diff6and7(data, h): #First problem: differentiate 6 from 7
    if data[3] * data[10] > h: # Function: f(MBS, SCGr) = MBS * SCGr > h
    # h = 431 100% accuracy
        sp = 7 #if f(MBS, SCGr) > h, then species_num is probably 7
    else: #f(MBS, SCGr) <= 48 
        sp = 6 #if f(MBS, SCGr) > h, then species_num is probably 6
    if data[0] == 7 and sp == 7: # if real species_num is 7 and predict species_num is 7
        return 11 #11 is a to determine a variable outside the function
    elif data[0] == 6 and sp == 6: # if real species_num is 6 and predict species_num is 6
        return 22 #same as 11
    elif data[0] == 6 and sp == 7: # if real species_num is 6 and predict species_num is 7
        return 21 #same as 11
    elif data[0] == 7 and sp == 6: # if real species_num is 7 and predict species_num is 6
        return 12 #same as 11

right1 = 0  #variable: number of correct species 6
right2 = 0  #variable: number of correct species 7
wrong1 = 0  #variable: number of incorrect species 6(real species_num)
wrong2 = 0  #variable: number of incorrect species 7(real species_num)
'''
#Code to find the highest percentage by looping through h
percent = {} #container includes the h-value and the percentage of correct lizards
for j in range(0, 200): #Try values of h    
    for i in range(564): #Loop through all the lizards to determine if it is correct or not
        lizard = list(data[i]) #Get the lizard data from the array
        if lizard[0] != 6 and lizard[0] != 7: #Exclude lizards that is not 6 and 7
            continue
        result = diff6and7(lizard, j) #Use the function to determine if it is correct
        if result == 11: 
            right1 +=
        elif result == 22:
            right2 += 1
        elif result == 12:
            wrong1 += 1
        elif result == 21:
            wrong2 += 1
    percent[j] = (right1 + right2)/(right1 + right2 + wrong1 + wrong2) #Caculate the percent: Correct/Total
    right1 = 0 # Reset the variables
    right2 = 0
    wrong1 = 0
    wrong2 = 0

max_num = 0 # Vairable: help to store the maxnium percentage

for i in percent.items(): #Loop through percent[dictionary]
    if max_num < i[1]: #Detremine the biggest percentage
        max_num = i[1] 
        key = i[0] #Get key

print(key, max_num)
'''
'''
#Code to Show the variables when h is given
for i in range(564): #Simliar function as above code
        lizard = list(data[i])
        if lizard[0] != 6 and lizard[0] != 7:
            continue
        result = diff6and7(lizard, 431)
        if result == 11:
            right1 += 1
        elif result == 22:
            right2 += 1
        elif result == 12:
            wrong1 += 1
        elif result == 21:
            wrong2 += 1

percent = (right1 + right2)/(right1 + right2 + wrong1 + wrong2) #caculate percentage

print(f"Correct identifed species 7: {right1}")
print(f"Correct identifed species 6: {right2}")
print(f"Wrongly identifed species 7: {wrong1}")
print(f"Wrongly identifed species 6: {wrong2}")
print(f"correct percentage: {percent}")
'''
#Following Codes are simliar to the above code example
#They have simliar structure, but different values

def diff1and2(data, h):#Second problem: differentiate 1 from 2
    if data[18] * data[12] * data[13] * data[9] * data[25] > h:
        #function(SCSr, MTr, PA, HL, HFL) = SCSr * MTr * PA * HL * HFL > h
        #Below are functions, and their best h and percentage pair
        #Strong values: 9 12 13 16 18 25
        #4+10+16+18+19+24+25 170 81.4%
        #_+10+16+18+19+24+25 148 78.3%
        #4+__+16+18+19+24+25 159 80.6%
        #4+10+__+18+19+24+25 117 79.1%
        #4+10+16+__+19+24+25 151 84.5%
        #4+10+16+18+__+24+25 157 83.7%
        #4+10+16+18+19+__+25 152 83.7%
        #4+10+16+18+19+24+__ 141 80.6%
        #4+10+16+__+__+24+25 138 84.5%
        
        #13*9*25 305 89.9%
        #13*9*25*18 5534 90.7%
        #12*13*16*18 4400 90.7%
        #3*12*13*18 5292 89.9%
        #12*13*18*25 2527 92.2%
        #12*13*9*25 749 92.2%
        #12*13*9*18 471 92.2%
        #9*12*13*18*25 12701 93.0% BEST
        sp = 1 #if f(SCSr, MTr, PA, HL, HFL) > h, it is probably species 1
    else: 
        sp = 2
    if data[0] == 1 and sp == 1:
        return 11
    elif data[0] ==2 and sp == 2:
        return 22
    elif data[0] == 2 and sp == 1:
        return 21
    elif data[0] == 1 and sp == 2:
        return 12
    
right1 = 0
right2 = 0
wrong1 = 0
wrong2 = 0
'''
#Code to find the highest percentage by looping through h
percent = {}
for j in range(0, 200):    
    for i in range(564):
        lizard = list(data[i])
        if lizard[0] != 1 and lizard[0] != 2:
            continue
        result = diff1and2(lizard, j)
        if result == 11:
            right1 += 1
        elif result == 22:
            right2 += 1
        elif result == 12:
            wrong1 += 1
        elif result == 21:
            wrong2 += 1
    percent[j] = (right1 + right2)/(right1 + right2 + wrong1 + wrong2)
    right1 = 0
    right2 = 0
    wrong1 = 0
    wrong2 = 0

max_num = 0
for i in percent.items():
    if max_num < i[1]:
        max_num = i[1]
        key = i[0]
print(key, max_num)
'''

#Code to Show the variables when h is given
for i in range(564):
        lizard = list(data[i])
        if lizard[0] != 1 and lizard[0] != 2:
            continue
        result = diff1and2(lizard, 12701)
        if result == 11:
            right1 += 1
        elif result == 22:
            right2 += 1
        elif result == 12:
            wrong1 += 1
        elif result == 21:
            wrong2 += 1

percent = (right1 + right2)/(right1 + right2 + wrong1 + wrong2)

print(f"Correct identifed species 1: {right1}")
print(f"Correct identifed species 2: {right2}")
print(f"Wrongly identifed species 1: {wrong1}")
print(f"Wrongly identifed species 2: {wrong2}")
print(f"correct percentage: {percent}")


def diff345(data, h): #Third problem: differentiate 3 from 4 from 5
    if data[7] <= 11: #function(FPNr) = FPNr <= 11
        #Using problem 1's conclusion
        sp = 5
    elif data[6] < h: ##function(GSN) < h
        #h = 26.1 95.6% accuracy
        sp = 3
    else:
        sp = 4
    if data[0] == 3 and sp == 3:
        return 33
    elif data[0] == 3 and sp != 3:
        return 30
    elif data[0] == 4 and sp == 4:
        return 44
    elif data[0] == 4 and sp != 4:
        return 40
    elif data[0] == 5 and sp == 5:
        return 55
    elif data[0] == 5 and sp != 5:
        return 50
   
right3 = 0
right4 = 0
right5 = 0
wrong3 = 0
wrong4 = 0
wrong5 = 0
'''
#Code to find the highest percentage by looping through h
percent = {}
for j in range(200, 300):    
    for i in range(564):
        lizard = list(data[i])
        if lizard[0] != 3 and lizard[0] != 4 and lizard[0] != 5:
            continue
        result = diff345(lizard, j/10)
        if result == 33:
            right3 += 1
        elif result == 44:
            right4 += 1
        elif result == 55:
            right5 += 1
        elif result == 30:
            wrong3 += 1
        elif result == 40:
            wrong4 += 1
        elif result == 50:
            wrong5 += 1
    percent[j/10] = (right3 + right4 + right5)/(right3 + right4 + right5 + wrong3 + wrong4 + wrong5)
    right3 = 0
    right4 = 0
    right5 = 0
    wrong3 = 0
    wrong4 = 0
    wrong5 = 0

max_num = 0
for i in percent.items():
    if max_num < i[1]:
        max_num = i[1]
        key = i[0]
print(key, max_num)
'''
'''
#Code to Show the variables when h is given
for i in range(564):
        lizard = list(data[i])
        if lizard[0] != 3 and lizard[0] != 4 and lizard[0] != 5:
            continue
        result = diff345(lizard, 26.1)
        if result == 33:
            right3 += 1
        elif result == 44:
            right4 += 1
        elif result == 55:
            right5 += 1
        elif result == 30:
            wrong3 += 1
        elif result == 40:
            wrong4 += 1
        elif result == 50:
            wrong5 += 1
percent = (right3 + right4 + right5)/(right3 + right4 + right5 + wrong3 + wrong4 + wrong5)

print(f"Correct identifed species 3: {right3}")
print(f"Correct identifed species 4: {right4}")
print(f"Correct identifed species 5: {right5}")
print(f"Wrongly identifed species 3: {wrong3}")
print(f"Wrongly identifed species 4: {wrong4}")
print(f"Wrongly identifed species 5: {wrong5}")
print(f"correct percentage: {percent}")
'''
