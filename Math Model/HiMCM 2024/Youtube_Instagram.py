def average(people, percen, age):
    total_age = 0
    for i in range(len(percen)):
        total_age += people * percen[i] * age[i]
    average = total_age / people
    return average


age = [20, 30, 40, 50, 60, 70]
y_f = 2.70 * 10**9
y_p = [0.157, 0.215, 0.179, 0.129, 0.092, 0.092]

i_f = 2 * 10**9
i_p = [0.313, 0.31, 0.164, 0.09, 0.048, 0.030]

age_t = [15, 20, 30, 43, 60]
t_f = 586 * 10**6
t_p = [0.025, 0.345, 0.354, 0.198, 0.078]

print(f"Youtube followers average age: {average(y_f, y_p, age)}")
print(f"Instagram followers average age: {average(i_f, i_p, age)}")
print(f"Twitter followersaverage age: {average(t_f, t_p, age_t)}")
