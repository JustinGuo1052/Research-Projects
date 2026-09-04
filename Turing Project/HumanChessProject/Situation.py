
def situation(k, round, total_round, points, color):
    color_advantage = 0.1
    return k * (1 + 2 * ((round - 1) / 2 - points)) * (1 / (total_round - round + 1)) * (color * (1 + color_advantage) + (1 - color) * (1 - color_advantage))

# pregame factors
'''
1. Player's style (p)
2. Color of match (c)
3. Opponent's strength (e)
5. Urgency of winning (w)
'''
# post game factors