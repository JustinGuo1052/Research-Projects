import chess.engine
import chess.pgn
import chess
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.collections import LineCollection
from Desire import ana_desire
import time
from Situation import situation
from Risky2 import ana_risk


def check_stable(array):
    mean = sum(array) / len(array)
    var = 0
    for i in array:
        var += (i - mean)**2
    var /= len(array)
    sd = var ** 0.5
    # print(sd)
    if sd < 0.01:
        return True
    else:
        return False


def eval_time(engine, board, limit_depth):
    score = []
    with engine.analysis(board, chess.engine.Limit(depth=limit_depth)) as analysis:
        for info in analysis:
            # if type(info.get("score")) is chess.engine.PovScore:
            if not info.get("score"):
                continue
            # print(info.get("score").white().score())
            if type(info.get("score").white().score()) is int:
                score.append(math.tanh(info.get("score").white().score() / 100))
            else:
                score.append(1)
            stabled = False
            if len(score) > 8:
                stable_sample = score[-8:]
                stabled = check_stable(stable_sample)
            if stabled:
                break
    return score


def plotting(name, array, ymin, ymax, xmin, xmax):
    plt.figure()
    plt.plot(array)
    plt.ylim(ymin, ymax)
    plt.xlim(xmin, xmax)
    plt.xticks(range(xmin, xmax))
    plt.savefig(name)


def analyze_type(engine, directory, file_name, depth):
    f = open(f"{directory}/{file_name}.txt")
    lines = f.readlines()
    for i in range(len(lines)):
        fen = lines[i]
        b = chess.Board(fen)
        d = depth
        # s = ana_risk(stockfish, b)
        plotting(f"{directory}/{file_name}{i}.png", s, -1.1, 1.1, 0, d)
    f.close()


path = "/Users/iby/Desktop/classes/科创/Turing Project/HumanChessProject/stockfish/stockfish-macos-m1-apple-silicon"
stockfish = chess.engine.SimpleEngine.popen_uci(path)

t = ['Tactic', 'Lock', 'Complex']  # drawn

for i in t:
    analyze_type(stockfish, i, i, 40)

stockfish.close()

