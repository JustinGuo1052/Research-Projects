import math as m
a = m.sqrt(2)
s = 100
numbers = []
pi = 3.141592653589

q = 0
for i in range(1000):
    q = i/100
    numbers.append(q)

for x in numbers:
    for y in numbers:
        if 349.9 < x**2*pi*y + pi/4*x**2*(3*a*x - x/2)/3 < 350.1:
            if y >= 2:
                print(x, y)
                print(x**2*pi*y + pi/4*x**2*(3*a*x - x/2)/3)
                print("")
                if x + y < s:
                    s = x + y
print(s)
                
            
            

            
            
            
            
    
