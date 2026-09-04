Ttwo = 127
Tone = 22
k = 2

a = []
x = 0
for i in range(100):
    x = x + 1
    a.append(x)
for s in a:
    L = float(s)
    q = -k*(Ttwo - Tone)/L
    if q  > -5:
        print(L, q)
    
    
