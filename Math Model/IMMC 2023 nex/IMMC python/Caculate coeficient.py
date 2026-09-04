
for x in range(0, 21):
    for y in range(-20, 1):
        for z in range(0, 21):
            a, b, c = x/10, y/10, z/10
            if a == 0 or b == 0 or c == 0:
                continue
            if 1.32 <= a**2 + b**2 + c**2 <= 1.34:
                print(a, b, c)
                print(a**2 + b**2 + c**2)
        

#0.1 -0.4 0.4
#0.2 -0.5 0.1
#0.5 -0.2 0.2

    #0.7 -0.6 0.7


import random

def benefit():    
    eco = random.randint(1000000000, 3000000000)
    env = random.randint(900000, 1000000)
    hum = random.randint(0, 20)
    
    
    return int(5/8 * (0.7 * eco / 10**7 - 0.6 * env / 10**4 + 0.7 * hum))
num = []
for i in range(1000):
    num.append(benefit())

print((sum(num) / len(num)))
print(min(num), max(num))

    
                            
                        
                        
                         
            
















                
