import chess.engine
import chess.pgn
import chess
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.collections import LineCollection
from Operation import mean_change


def risky(engine, b):
    # The function to find the riskiness of a move
    s = []
    with engine.analysis(b, chess.engine.Limit(depth=15)) as analysis:
        # Get some info then stop
        for info in analysis:
            if type(info.get("score")) is chess.engine.PovScore and info.get("depth") >= 5:
                s.append(info.get("score").white().score())
                if not(type(s[len(s)-1]) is int):
                    s.pop()

    # print(s)
    ac = mean_change(s)
    # print(ac)
    # ac = inte(s)
    # print(ac, info['pv'][0])
    # print(ac)
    try:
        return ac, info['pv'][0], s[-1]
    except KeyError:
        return ac, chess.Move.from_uci("e2e4"), s[-1]

def ana_risk(engine, pgn):
    with open(pgn) as pgn_file:
        game = chess.pgn.read_game(pgn_file)
    board = game.board()

    starter = risky(board)
    human_ac = [starter[0]]
    engine_ac = [starter[0]]
    equal = []
    gmain = list(game.mainline_moves())
    previous = 0.2
    print(f"Game {game.headers['Round']}")

    for i in range(len(gmain) - 2):
        move = gmain[i]
        e_ac = risky(engine, board)

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
            print(f"Turn: {turn}, Move: {move}, Riskyness added to pos:  {human_ac[-1] - human_ac[-2]:.2f}, Riskyness of pos: {human_ac[-1]:.2f}, Eval: {h_ac[2]}")
        else:
            print(f"Turn: {turn}, Move: {move}, Riskyness added to pos: {human_ac[-1] - human_ac[-2]:.2f}, Riskyness of pos: {human_ac[-1]:.2f}, Eval: {h_ac[2]}")

        if not equal_pos:
            print(f"Number of moves analyzed: {i}")
            break
        # print(move, h_ac[0], e_ac[1], e_ac[0])

    print()

    white_human_ac = []
    black_human_ac = []
    white_computer_ac = []
    black_computer_ac = []

    for i in range(1, len(human_ac)):
        if i % 2 == 1:
            white_human_ac.append(human_ac[i] - human_ac[i - 1])
            white_computer_ac.append(engine_ac[i] - human_ac[i - 1])

        else:
            black_human_ac.append(human_ac[i] - human_ac[i - 1])
            black_computer_ac.append(engine_ac[i] - human_ac[i - 1])

    color_code = []
    for j in range(len(human_ac) - 1):
        if j % 2 == 0:
           color_code.append(1)
        else:
            color_code.append(0)
    fig2, ax2 = plt.subplots()
    line = colored_line_between_pts(list(range(len(human_ac))), human_ac, color_code, ax2, linewidth=2)
    fig2.colorbar(line, ax=ax2, label="white: R, black: B")
    ax2.set_xlim(0, len(human_ac))
    ax2.set_ylim(0, 10)
    plt.xticks(list(range(0, len(human_ac), 4)))
    plt.savefig(f"RiskyofPosition{game.headers['Round']}.png")

    a_w_h_ac = sum(white_human_ac) / len(white_human_ac)
    a_b_h_ac = sum(black_human_ac) / len(black_human_ac)
    a_w_e_ac = sum(white_computer_ac) / len(white_computer_ac)
    a_b_e_ac = sum(black_computer_ac) / len(black_computer_ac)
    print(f"average white riskyness: {a_w_h_ac}", end="     ")
    print(f"average black riskyness: {a_b_h_ac}")
    print(f"average computer riskyness for white: {a_w_e_ac}", end="     ")
    print(f"average computer riskyness for black: {a_b_e_ac}")
    return a_w_h_ac, a_b_h_ac