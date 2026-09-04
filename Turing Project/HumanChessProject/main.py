import chess.engine
import chess.pgn
import chess
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.collections import LineCollection
from Risky import ana_risk
from Desire import ana_desire
import time
from Situation import situation
from Risky2 import eval_risk


path = "/Users/iby/Desktop/classes/科创/Turing Project/HumanChessProject/stockfish/stockfish-macos-m1-apple-silicon"
engine = chess.engine.SimpleEngine.popen_uci(path)
pgn = f"Ding_Ian/6.pgn"
ana_risk(engine, pgn)
engine.quit()


'''
ding_score = 0
ian_score = 0
Ding_white = False

middle_game = [37 * 2, 29 * 2, 27 * 2, 46 * 2, 43 * 2, 43 * 2, 37 * 2, 42 * 2, 33 * 2, 18 * 2, 22 * 2, 37 * 2, 27 * 2, 18 * 2]

order = list(range(1, 15))
white_riskyness = []
black_riskyness = []
for i in range(0, len(order)):
    pgn = f"Ding_Ian/{order[i]}.pgn"
    print(ding_score, ian_score)
    sit_ding = situation(1, i + 1, 14, ding_score, Ding_white)
    sit_ian = situation(1, i + 1, 14, ian_score, not Ding_white)

    if Ding_white:
        print(f"white situation: {sit_ding}")
        print(f"black situation: {sit_ian}")
    else:
        print(f"white situation: {sit_ian}")
        print(f"black situation: {sit_ding}")

    riskyness = ana_risk(pgn)
    white_riskyness.append(riskyness[0])
    black_riskyness.append(riskyness[1])

    game = chess.pgn.read_game(open(pgn))

    r_score = game.headers["Result"]
    w_point = 0
    b_point = 0
    if r_score == "1/2-1/2":
        w_point = 0.5
        b_point = 0.5
    elif r_score == "1-0":
        w_point = 1
    elif r_score == "0-1":
        b_point = 1

    if Ding_white:
        ding_score += w_point
        ian_score += b_point
    else:
        ding_score += b_point
        ian_score += w_point
    Ding_white = not Ding_white


engine.quit()

'''

# open up the specific fen
'''
fen_Rg6 = "8/6pk/6rp/p1p5/1b2Q3/4B1PP/4qP2/2R3K1 w - - 12 47"  # Ding-Nepo 18 1-0 'self-pin' risky
fen_h5 = "r1bq1rk1/3nppbp/P2p1np1/2pP3P/4P3/2N5/PPQ2PP1/R1B1KBNR b KQ - 0 10"  # Fedo-Salem 1 0-1 'sacrifice pawn' risky
fen_Ne5 = "r3qrk1/6bp/b2pp3/2p1n1Pp/4PP2/2N3N1/PPQ5/R1B1K2R w KQ - 2 19"  # Fedo-Salem 1 0-1 'sacrifice knight' risky
fen_Rd4 = "b2r3r/k4p1p/p2q1np1/NppP4/3R1Q2/P4PPB/1PP4P/1K2R3 b - - 0 24"  # Kas-Topa 1 1-0 'sacrifice rook' risky
fen_cd = "b2r3r/k4p1p/p2q1np1/Np1P4/3p1Q2/P4PPB/1PP4P/1K2R3 w - - 0 25"  # Kas-Topa 1 1-0 'accept sacrifice' risky
fen_Bh6 = "r1bqk2r/p2nppbp/2pp1npB/1p6/3PP3/2N2P2/PPPQN1PP/R3KB1R b KQkq - 3 8"  # Kas-Topa 1 1-0 'normal trade' not risky
fen_Bb7 = "r2qk2r/pb1npp1p/2pp1npQ/1p6/3PP3/2N2P2/PPP1N1PP/R3KB1R w KQkq - 1 10" # Kas-Topa 1 1-0 'normal devlopment' not risky

ac_Rd4 = risky(chess.Board(fen_Rd4), 10)
ac_cd = risky(chess.Board(fen_cd), 10)
ac_Bh6 = risky(chess.Board(fen_Bh6), 10)
ac_Bb7 = risky(chess.Board(fen_Bb7), 10)

plt.show()
'''
'''
with open("Fedoseev_ Salem.pgn") as pgn_file:
    game = chess.pgn.read_game(pgn_file)
board = game.board()

human_ac = []
engine_ac = []
gmain = list(game.mainline_moves())

print(gmain)
for i in range(len(gmain) - 2):
    move = gmain[i]
    e_ac = risky(board, 5)
    board.push(move)
    if move == e_ac[1]:
        h_ac = e_ac
    else:
        h_ac = risky(board, 5)
    human_ac.append(h_ac[0])
    engine_ac.append(e_ac[0])
    print(move, h_ac[0], e_ac[1], e_ac[0])

white_human_ac = []
black_human_ac = []
for i in range(len(human_ac)):
    if i % 2 == 0:
        white_human_ac.append(human_ac[i])
    else:
        black_human_ac.append(human_ac[i])

a_w_h_ac = sum(white_human_ac) / len(white_human_ac)
a_b_h_ac = sum(black_human_ac) / len(black_human_ac)
a_e_ac = sum(engine_ac) / len(engine_ac)

print(a_w_h_ac)
print(a_b_h_ac)
print(a_e_ac)

plt.figure()
plt.plot(human_ac)
plt.plot(engine_ac)
plt.show()
engine.quit()
'''
'''
# opening up the specific pgn
with open("Kasparov_Topalov.pgn") as pgn_file:
    game = chess.pgn.read_game(pgn_file)
board = game.board()

# processing each move of the game
for move in game.mainline_moves():
    if move.uci() == 'c5d4':
        info = engine.analyse(board, chess.engine.Limit(time=2.0))
        c_move = info['pv'][0]
        c_score = info['score']
        print(board.san(c_move), c_score)
    # info = engine.analyse(board, chess.engine.Limit(time=2.0))
    # print(f"Player move: {board.san(move)}, Computer Move: {board.san(info['pv'][0])}")
    board.push(move)
    if move.uci() == 'c5d4':
        info = engine.analyse(board, chess.engine.Limit(time=2.0))
        print('cxd4', info['score'])
    # print(board)
engine.quit()
'''
