from chessboard import *
import collections


chess = collections.namedtuple('chess', ['soldier', 'general', 'vehicle', 'horse', 'elephant', 'officer', 'cannon'])

def initialization():
    init_chess = chess(soldier=((0, 3, 0), (0, 3, 2), (0, 3, 4), (0, 3, 6), (0, 3, 8), (1, 6, 0), (1, 6, 2), (1, 6, 4),
                                (1, 6, 6), (1, 6, 8)), general=((0, 0, 4), (1, 9, 4)),
                       vehicle = ((0, 0, 0), (0, 0, 8), (1, 9, 0), (1, 9, 8)),
                       horse=((0, 0, 1), (0, 0, 7), (1, 9, 1), (1, 9, 7)),
                       elephant=((0, 0, 2), (0, 0, 6), (1, 9, 2), (1, 9, 6)),
                       officer = ((0, 0, 3), (0, 0, 5), (1, 9, 3), (1, 9, 5)),
                       cannon=((0, 2, 1), (0, 2, 7), (1, 7, 2), (1, 7, 7)))

    print(init_chess.soldier[0])



initialization()