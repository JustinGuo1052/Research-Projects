import chess.engine
import chess.pgn
import chess
import matplotlib.pyplot as plt
import math
import time

def situation(k, round, total_round, points, color):
    color_advantage = 0.1
    return k * (1 + 2 * ((round - 1) / 2 - points)) * (1 / (total_round - round)) * (color * (1 + color_advantage) + (1 - color) * (1 - color_advantage))

# pregame factors
'''
1. Player's style (p)
2. Color of match (c)
3. Opponent's strength (e)
5. Urgency of winning (w)
'''
# post game factors


def mean_change(s):
    length = len(s)
    # print(length)
    l_sum = 0
    for i in range(0, length - 1):
        l_sum += abs(s[i + 1] - s[i])

    # print(l_sum, amplitude)
    return l_sum / length


def average_change(s):
    length = len(s)
    sum = 0
    amplitude = max(s) - min(s)

    if amplitude == 0:
        return 0
    for i in range(length - 1):
        sum += abs(s[i + 1] - s[i])

    return sum / amplitude

def inte(s):
    sum = 0
    for i in range(len(s) - 1):
        sum += 0.5 * 1 * (abs(s[i + 1]) + abs(s[i]))
    return sum

def gmean(arr):
    pro = 1
    for i in arr:
        if i == 0:
            continue
        pro *= i
    pro = math.pow(pro, 1 / len(arr))
    return pro

def risky(b, t):
    # The function to find the riskiness of a move
    s = []
    with engine.analysis(b, chess.engine.Limit(time=t)) as analysis:
        # Get some info then stop
        for info in analysis:
            if type(info.get("score")) is chess.engine.PovScore:
                s.append(info.get("score").white().score())
                if not(type(s[len(s)-1]) is int):
                    s.pop()

    # print(s)
    ac = mean_change(s)

    # print(ac)
    # ac = inte(s)
    # print(ac, info['pv'][0])
    # print(ac)
    return ac, s

path = "/Users/iby/Desktop/classes/科创/Turing Project/HumanChessProject/stockfish/stockfish-macos-m1-apple-silicon"
engine = chess.engine.SimpleEngine.popen_uci(path)

for i in range(1):
    # complex position choose: French Defense
    fen = "rnbqkbnr/ppp2ppp/4p3/3p4/3PP3/8/PPP2PPP/RNBQKBNR w KQkq - 0 1"

    board = chess.Board(fen)
    # print(board.legal_moves)
    move = ["e5", "Nc3", "exd5"]
    e_ac = risky(board, 20)
    plt.plot(range(len(e_ac[1])), e_ac[1], color='k')
    c = ['r', 'g', 'b']
    for i in range(len(move)):
        board = chess.Board(fen)
        board.push_xboard(move[i])
        h_ac = risky(board, 20)
        print(move[i], h_ac[0])
        plt.plot(range(len(h_ac[1])), h_ac[1], color=c[i])

    plt.show()


'''
1. 
e5 2.953488372093023
Nc3 2.7755102040816326
exd5 2.3260869565217392
2. 
e5 1.9574468085106382
Nc3 1.8823529411764706
exd5 1.625
3.
e5 2.4375
Nc3 1.8979591836734695
exd5 1.7608695652173914
4. 
e5 2.234042553191489
Nc3 2.18
exd5 2.311111111111111
'''

