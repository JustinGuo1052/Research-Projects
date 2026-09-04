a = []
w = 1
x = 0
for i in range(100):
    x = x + 0.1
    a.append(x)



R = 0
h = 0
for s in a:
    for t in a:
        R = float(s)
        h = float(t)
        v = 1/3*3.14*(3*R-h)*h**2/2 + 1/3*3.14*(3*(R+w)-(h+w))*(h+w)**2/2 - 1/3*3.14*(3*R-h)*h**2/2  
        if 351 > v > 349:
            print(R, h, (1/3*3.14*(3*(R+w)-(h+w))*(h+w)**2/2 - 1/3*3.14*(3*R-h)*h**2/2) /R/R/3.14, v)                
        


