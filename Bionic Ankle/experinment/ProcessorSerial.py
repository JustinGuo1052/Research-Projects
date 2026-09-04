import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import pandas as pd



file = open("ReadSerial.txt")

content = file.readlines()

time = []
F = []
# print(len(content))
for i in range(len(content)):
    if (content[i] == "\n"):
        continue
    time.append(i + 1)

    # y = 0.45x - 0.89
    
    F.append(0.45 * int(content[i]) - 10.89)

for i in range(len(F)):
    F[i] = -F[i]


    
F = np.array(F)
time = np.array(time)

X_Y_Spline = make_interp_spline(time, F)
time_ = np.linspace(time.min(), time.max(), 1500)
F_ = X_Y_Spline(time_)


time_A = []  
A = []
eplison = 1 * 10 ** -6


start = 110
end = 480

for i in range(start, end):
    dx = (F[i + 1] - F[i]) / 2
    if (abs(dx) < eplison):
        A.append(F[i])
        time_A.append(i)

# for i in range(len(A)):
    # print(time_A[i], round(A[i], 3))
    

plt.figure(0, (20, 8))

mini = 0
maxi = 100

for i in range(len(time_)):
    time_[i] -= 110
    time_[i] /= 100

inter = 5
plt.grid()
plt.ylim((-55, 5))
plt.yticks(range(-55, 10, inter))
plt.xlim((0, 4))
plt.xticks(range(0, 5, 1))
plt.title("Comparision between Experinment and ADAMS simulation Plot Force vs Time")
plt.xlabel("Time(s)")
plt.ylabel("Spring Force(N)")
plt.plot(time_, F_, label = 'experinment')

dfs = []

dfs = pd.read_csv(f"simu_foot.tab", sep='\t', header=1)
dfs.columns = ['time', 'force']

start_time = dfs['time'].iloc[74]
dfs = dfs.iloc[74:]
for i in range(len(dfs)):
    dfs['time'].iloc[i] -= start_time
# 74
plt.plot(dfs['time'], dfs['force'], label = 'adams simulation')
plt.legend()

plt.savefig("F-t graph")

df = pd.DataFrame([time_, F_])

df.to_excel("E_F_T.xlsx")
print("done")

'''
0: 0

1: 24

2.5: 57

https://math.libretexts.org/Courses/Cosumnes_River_College/Math_420%3A_Differential_Equations_(Breitenbach)/06%3A_Applications_of_Linear_Second_Order_Equations/6.02%3A_Spring-Mass_Problems_(With_Damping)



'''


'''
k = 0.330403
m_ori = 1.5
r_ori = 32.3
r_spr = 14.4

m = m_ori * r_ori / r_spr

c = 2 * m * k

print(c)
'''













