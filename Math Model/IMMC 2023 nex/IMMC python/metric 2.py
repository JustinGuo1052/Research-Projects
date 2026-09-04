
def economics(cost_upfront, earn, cost_sustained):
    #Amount fo money used for the project to sustain itself
    GDP = cost_upfront + (cost_sustained + earn) * 10
    return int(GDP)

def lands(land, environment):
    #Assume 1 block of crop land is priced 1, forest is prices as trees which is 210
    land_after = environment[0]
    depletion = environment[1]
    f2c = land['forest'] - land_after['forest']
    f2c_minus = 210
    return -((f2c*f2c_minus)  + (land_after['crop'] * (1 - depletion)**10))    

def humans(jobs, attraction, tourism):
    #assume jobs_max ==> 15, tourism_max ==> 6000
    tourism_max = 6000
    jobs_max = 15
    tourism_co = jobs_max / tourism_max
    return jobs + attraction + tourism * tourism_co
 
#local coefficient = 1
#vacation coefficient = 1/3
#tourism = local * local coefficient + vacation * vacation coefficient = 36000 * 0.1 * 1 + (265.5 * 10**6 * 10**-4) * 1/3 = 3600 * 1 + 26550 * 1/3 = 12450 people 
#tourism = local + vacation
#local = local people * cost_upfront * time * 10        time = 1
#vacation = vacation people * cost_upfront * importance * time         importance = 0.01, time = 0.01
#local = 36000 * 2700000 * 1

def benefit(land, cost_upfront, jobs, attraction, cost_sustained, earn, environment, tourism):    
    #land should be in a dict: describing each type of block and how much in each type | {crops: x, forest: y, wetland: z}
    '''visualize'''
    #cost_upfornt should be a number: describing the cost of building the land | $money
    '''reasearch'''
    #jobs should be a dict: describing how much different jobs there are in the land | human 
    '''research'''
    #attraction should be a number: describing how much people will come to this farm | human
    '''unknown'''
    #earn should be a number: it describes how much money the land use will make per year | $money
    '''research'''
    #cost_sustained should be a number: describing how much money should be used to maintain the land and give the salary per year | $money
    '''research'''
    #environment should be a dict: describing each type of block and how much in each type after stuff ({crops: (x + a), forest: y - a, wetland: z}, q)
    '''research'''
    #tourism should be a number: describing how much people will vist the land per year | human
    '''estimate'''
    eco = economics(cost_upfront, cost_sustained, earn)
    env = lands(land, environment)
    hum = humans(jobs, attraction, tourism)
    eco = int(eco / (10**7))
    env = int(env / (10**4))
    hum = int(hum)
    return int(5/8 * (0.7 * eco + 0.6 * env + 0.7 * hum))

land = {"crop": 2961, "forest": 5065, "wetland": 2299}
#1 block = 230 m^2
salary = 67521

# Solar Farm 163 MW solar panel

consumption =  7.2 # 60000 households in the vicinity
production = 28.3 #568*5/25/4
requirement = consumption/production

cost_upfront = 163000000 -210*5065
earn = 568 * 450000 #38699460 / 16000 * 1000 / 40000 * 163 / 568 * 450000 / 163 * 2146 * 1000 * 0.24 
cost_sustained = salary * 10 + 300 #300 + 10 * 67,521

environment = ({"crop": 2961 + 5065, "forest": 5065 - 5065, "wetland": 2299}, 1)
jobs = 10
tourism = 0
attraction = jobs/10 + salary/100000


'''
print(economics(cost_upfront, earn, cost_sustained))
print(lands(land, environment))
print(humans(jobs, attraction, tourism))
'''
print(benefit(land, cost_upfront, jobs, attraction, cost_sustained, earn, environment, tourism))

#Crop farm Lettuce farming for 2.3 km^2 (569 acres)

consumption = 136000 
prduction = 568 * 12000 * (365 / 20)
requirement = consumption/production

cost_upfront = 630000 - 210*5065 #310,000 + 300,000 + 20,000
earn = 10400 * 568 * (365 / 20) #$2.09 * 568 * 12000 * (365 / 20) / #$10400 * 568 * (365 / 30) 
cost_sustained = 568 * 9000 * (365 / 30) + 10 * salary #568 * 9000 * (365 / 30) + 5 * 67521
environment = ({"crop": 2961 + 5065, "forest": 5065 - 5065, "wetland": 2299}, 1)
jobs = 10
attraction = jobs/10 + salary/100000
tourism = 0

'''
print(economics(cost_upfront, earn, cost_sustained))
print(lands(land, environment))
print(humans(jobs, attraction, tourism))
'''
print(benefit(land, cost_upfront, jobs, attraction, cost_sustained, earn, environment, tourism))

