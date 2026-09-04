
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("ratings.xlsx")
print(df)
index_number = 10
index = ['FollowersOnInstagram', 'FollowersOnYoutube', 'MaleFemaleRatio', 'MemberNationNumbers', 'ContinentalSpan', 'VRIncorporation', 'Safety', 'SustainabilityFactor', 'NumberOfAntiDopingSamples', 'FollowersOnTwitter']
color = []

for i in range(23):
    color.append('g')
for i in range(5):
    color.append('r')
for i in range(3):
    color.append('g')
for i in range(14):
    color.append('r')

    
result = df.loc[:, 'FollowersOnInstagram']

# result = df.loc['FollowersOnInstagram']
for i in range(10):
    result = df.loc[:, index[i]]
    plt.figure()
    plt.title(index[i])
    plt.scatter(range(45), result, c = color)
    plt.savefig(index[i])
