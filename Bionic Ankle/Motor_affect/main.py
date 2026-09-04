import pandas as pd
import matplotlib.pyplot as plt

path_to_folder = "/Users/iby/Desktop/classes/科创/脚踝/Motor_affect/F&S_-180_-180"
df_h = pd.read_excel(path_to_folder + "/F&S_-180_0RM.xlsx")
df_l = pd.read_excel(path_to_folder + "/F&S_0_-180RM.xlsx")
df_b = pd.read_excel(path_to_folder + "/F&S_-180_-180.xlsx")

rows_to_drop = df_h.index[df_h.index % 5 != 0]  # Select rows where mod 5 is not 0
df_h = df_h.drop(rows_to_drop)
df_h = df_h.reset_index()

df_hl = pd.concat([df_h, df_l], ignore_index=True)


print(df_h.head())
print(df_l.head())
print(df_hl.head())
print(df_b.head())

print(len(df_hl["Time"]))
print(len(df_b["Time"]))

plt.figure(1)
plt.plot(df_hl["Time"], df_hl["front"], c='b')
plt.plot(df_b["Time"], df_b["front"], c='r')
plt.show()
'''
plt.figure(2)
plt.plot(df_hl.loc[:, "Time"], df_hl.loc[:, "side"])
plt.plot(df_b.loc[:, "Time"], df_b.loc[:, "side"])
plt.show()
'''
