import matplotlib.pyplot as plt

f = open("infomation.txt", 'r')

time = []
roll = []
pitch = []

for i in range(30):
    line = f.readline()
    line = line[:-1]
    line = line.split()
    print(line)
    time.append(float(line[0]))
    roll.append(float(line[1]))
    pitch.append(float(line[2]))

average_pitch = 0
average_roll = 0

for i in range(30):
    average_pitch += pitch[i]
    average_roll += roll[i]

average_pitch /= 30
average_roll /= 30

print(average_pitch, average_roll)
print(time)
print(roll)
print(pitch)

plt.figure(1)

plt.plot(time, pitch)

plt.title("The Deviation of pitch after 1 second")
plt.xlabel("time(ms)")
plt.ylabel("degrees(°)")
plt.savefig("pitch")

plt.figure(2)
plt.plot(time, roll)

plt.title("The Deviation of roll after 1 second")
plt.xlabel("time(ms)")
plt.ylabel("degrees(°)")
plt.savefig("roll")



