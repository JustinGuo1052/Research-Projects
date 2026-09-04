import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
'''
angle = [135, 180, 225]

motor = ["LOW", "HIGH", "BOTH"]
add_slope = []
com_slope = []
add_slope = [0, 0, 0]
for m in motor:
    np_time = []
    np_angle = []
    slopes = []
    intercepts = []
    for i in range(len(angle)):
        df = pd.read_csv(f"{m}_{angle[i]}.tab", sep='\t', header=1)
        # print(df.columns)
        np_time.append(np.array(df["Time      "]))
        np_angle.append(np.array(df['.JOINT_14.Ax_Ay_Az_Projection_Angles.Z']))
        slope, intercept = np.polyfit(np_time[i], np_angle[i], 1)
        slopes.append(abs(slope))
        intercepts.append(intercept)
        if m != "BOTH":
            add_slope[i] += abs(slope)
        else:
            com_slope.append(abs(slope))

print(add_slope)
print(com_slope)
plt.plot(angle, com_slope, marker='.', linestyle='-', label="composition")
plt.plot(angle, add_slope, marker='.', linestyle='-', label="addition")
plt.title(f"MOTOR's rotational speed related with foot's rotational speed")
plt.xlabel("motor's rotational speed")
plt.ylabel("foot's rotational speed")
# plt.ylim([10, 20])
# plt.yticks(range(10, 22, 2))
plt.legend(loc="best")
plt.savefig(f"ADD_MOTOR_contrast.png")
'''

angle = [90, 135, 180, 225, 270, 315]

motor = ["BOTH"]
add_slope = []

for m in motor:
    np_time = []
    np_angle = []
    slopes = []
    intercepts = []
    for i in range(len(angle)):
        df = pd.read_csv(f"{m}_{angle[i]}.tab", sep='\t', header=1)
        # print(df.columns)
        np_time.append(np.array(df["Time      "]))
        np_angle.append(np.array(df['.JOINT_14.Ax_Ay_Az_Projection_Angles.Z']))
        slope, intercept = np.polyfit(np_time[i], np_angle[i], 1)
        slopes.append(abs(slope))
        intercepts.append(intercept)
    plt.plot(angle, slopes, marker='.', linestyle='-')
    plt.title(f"MOTOR's rotational speed related with foot's rotational speed")
    plt.xlabel("motor's rotational speed")
    plt.ylabel("foot's rotational speed")
    # plt.ylim([10, 20])
    # plt.yticks(range(10, 22, 2))
    plt.savefig(f"BOTH_MOTOR.png")

print(slopes)



'''
angle1 = [-180, 180]
angle2 = [-180]
n = len(angle1)

S_dfs = []
F_dfs = []

for i in range(2):
    for j in range(1):
        S_dfs.append(pd.read_csv(f"SADo{angle1[i]}_{angle2[j]}RM.txt", sep='\t', header=1))
        S_dfs[i].columns = ['time', 'angular_displacement']
        S_dfs[i]['time'] = S_dfs[i]["time"] * 100000 / 5

for i in range(2):
    for j in range(1):
        F_dfs.append(pd.read_csv(f"FADo{angle1[i]}_{angle2[j]}RM.txt", sep='\t', header=1))
        F_dfs[i].columns = ['time', 'angular_displacement']
        F_dfs[i]['time'] = F_dfs[i]["time"] * 100000 / 5


plt.figure()
for i in range(2):
    plt.plot(F_dfs[i]['time'], F_dfs[i]['angular_displacement'])
plt.xlabel("Time")
plt.ylabel("Angular Displacement")
plt.xlim([0, 5000])
plt.savefig(f"all2_compare_front.png")

plt.figure()
for i in range(2):
    plt.plot(S_dfs[i]['time'], S_dfs[i]['angular_displacement'])
plt.xlabel("Time")
plt.ylabel("Angular Displacement")
plt.xlim([0, 5000])
plt.savefig(f"all2_compare_side.png")
'''


