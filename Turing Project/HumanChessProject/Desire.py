import chess.engine
import chess.pgn
import chess
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.collections import LineCollection
from Risky import risky, ana_risk
import chess.engine
import chess.pgn
import chess
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.collections import LineCollection
from Risky import ana_risk
import time
from Situation import situation



def desire(engine, b):
    total = len(list(b.legal_moves))
    ana = engine.analyse(b, chess.engine.Limit(depth=15), multipv=total)
    all_moves = ana['multipv']
    a = 0
    for i in all_moves:
        a += abs(i['score'].score(mate_score=10000) - ana['score'].score(mate_score=10000)) / total
    return a


def ana_desire(engine, pgn):
    with open(pgn) as pgn_file:
        game = chess.pgn.read_game(pgn_file)
    board = game.board()
    gmain = list(game.mainline_moves())
    human_ac = []
    engine_ac = []

    for i in range(len(gmain) - 2):
        '''
        if i % 10 == 0:
            print('-', end="")
        '''
        move = gmain[i]
        e_ac = risky(board)

        # print(e_ac[2], equal_pos)
        # print(f"Turn: {i % 2 == 0}, S_co: {s_co}")
        board.push(move)
        h_ac = e_ac
        if move != e_ac[1]:
            h_ac = risky(board)
        # s_co = score_co(h_ac[2] / 100, i % 2 == 0)
        s_co = 1
        equal_pos = abs(h_ac[2]) <= 200
        turn = "black"
        if i % 2 == 0:
            turn = "white"
        human_ac.append(h_ac[0])
        engine_ac.append(e_ac[0])

        if human_ac[-1] - human_ac[-2] >= 0:
            print(
                f"Turn: {turn}, Move: {move}, Riskyness added to pos:  {human_ac[-1] - human_ac[-2]:.2f}, Riskyness of pos: {human_ac[-1]:.2f}, Eval: {h_ac[2]}")
        else:
            print(
                f"Turn: {turn}, Move: {move}, Riskyness added to pos: {human_ac[-1] - human_ac[-2]:.2f}, Riskyness of pos: {human_ac[-1]:.2f}, Eval: {h_ac[2]}")

        if not equal_pos:
            print(f"Number of moves analyzed: {i}")
            break
        # print(move, h_ac[0], e_ac[1], e_ac[0])
