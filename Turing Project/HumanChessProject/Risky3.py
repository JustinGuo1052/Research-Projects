import chess
import chess.engine
import chess.pgn
import math
import matplotlib.pyplot as plt


def eval_risk(engine, board):
    poss_score = []
    for i in board.legal_moves:
        board_copy = board.copy()
        board_copy.push(i)
        info = engine.analyse(board_copy, chess.engine.Limit(depth=15))
        a = info['score'].white().score(mate_score=1000)
        a /= 100
        poss_score.append(a)
    average_value = sum(poss_score) / len(poss_score)
    e = []
    s = 0
    for i in range(len(poss_score)):
        e.append((poss_score[i] - average_value) ** 2)
        s += (poss_score[i] - average_value) ** 2
    if s == 0:
        return 0
    p = []
    for i in range(len(e)):
        p.append(e[i] / s)

    r = 0
    for i in range(len(e)):
        try:
            r += e[i] * -math.log(p[i])
        except ValueError:
            print(f"Error: {p[i]}")

    return r

def ana_risk(engine, pgn):
    with open(pgn) as pgn_file:
        game = chess.pgn.read_game(pgn_file)
    board = game.board()

    previous = eval_risk(engine, board)
    game_main = list(game.mainline_moves())
    print(f"Game {game.headers['Round']}")

    game_risk = []
    for i in range(len(game_main)):
        move = game_main[i]
        board.push(move)
        # print(f"{i} {move}", end=" ")
        board_risk = (eval_risk(engine, board) + eval_risk(engine, board.mirror())) / 2
        game_risk.append(board_risk - previous)
        previous = board_risk
        # print(game_risk[-1])

    # move_s = int(len(game_main) / 2)
    # risk_max = max(game_risk)
    # plt.figure()
    # plt.subplot(211)
    colors = []
    c = True
    for i in range(len(game_risk)):
        if c:
            colors.append("white")
        else:
            colors.append('black')
        c = not c
    plt.figure()
    ax = plt.gca()
    ax.set_facecolor("green")
    plt.scatter(list(range(len(game_risk))), game_risk, c=colors)
    plt.savefig(f"Risk3Test{game.headers['Round']}.png")
    for i in range(len(game_main)):
        print(f"{colors[i]} - {game_main[i].uci()}: {game_risk[i]}")
    return game_risk


path = "/Users/iby/Desktop/classes/科创/Turing Project/HumanChessProject/stockfish/stockfish-macos-m1-apple-silicon"
engine = chess.engine.SimpleEngine.popen_uci(path)
pgn = "Tal_Petrosian/1.pgn"

average_riskyness_1 = []
average_riskyness_2 = []
for i in range(1, 15):
    pgn = f"Ding_Ian/{i}.pgn"
    a = ana_risk(engine, pgn)
    a_mean_0 = sum(a[0::2]) / len(a[0::2])
    a_mean_1 = sum(a[1::2]) / len(a[1::2])
    print(sum(a[0::2]) / len(a[0::2]), sum(a[1::2]) / len(a[1::2]))
    average_riskyness_1.append(a_mean_0)
    average_riskyness_2.append(a_mean_1)

My_interpretation = [True, True, True, True, True, True, True, True, False, True, False, True, True, True]


plt.figure()
move_s = 14
risk_max = max(average_riskyness_2 + average_riskyness_1)
plt.plot(list(range(1, move_s+1)), average_riskyness_1, c='red')
plt.xticks(range(1, move_s + 1, 1), rotation=45, ha='right')
plt.plot(list(range(1, move_s+1)), average_riskyness_2, c='blue')
plt.xlim(0, move_s + 1)
plt.ylim(0, risk_max)
plt.xticks(range(1, move_s + 1, 1), rotation=45, ha='right')
plt.show()
