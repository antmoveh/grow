from chessboard import *
import collections
import logging


class Launch:
    line1 = '{}__' * 8 + '{}'
    line2 = '|   ' * 8 + '|'
    line3 = "|      楚河             汉界    |"

    def __init__(self):
        self.chessboard = None


    def initialization(self):
        chess = collections.namedtuple('chess',
                                       ['soldier', 'general', 'vehicle', 'horse', 'elephant', 'officer', 'cannon'])
        cinit = chess(
            soldier=((0, 3, 0), (0, 3, 2), (0, 3, 4), (0, 3, 6), (0, 3, 8), (1, 6, 0), (1, 6, 2), (1, 6, 4),
                     (1, 6, 6), (1, 6, 8)), general=((0, 0, 4), (1, 9, 4)),
            vehicle=((0, 0, 0), (0, 0, 8), (1, 9, 0), (1, 9, 8)),
            horse=((0, 0, 1), (0, 0, 7), (1, 9, 1), (1, 9, 7)),
            elephant=((0, 0, 2), (0, 0, 6), (1, 9, 2), (1, 9, 6)),
            officer=((0, 0, 3), (0, 0, 5), (1, 9, 3), (1, 9, 5)),
            cannon=((0, 2, 1), (0, 2, 7), (1, 7, 1), (1, 7, 7)))
        s = [Soldier(c, x, y) for c, x, y in cinit.soldier]
        v = [Vehicle(c, x, y) for c, x, y in cinit.vehicle]
        g = [General(c, x, y) for c, x, y in cinit.general]
        h = [Horse(c, x, y) for c, x, y in cinit.horse]
        e = [Elephant(c, x, y) for c, x, y in cinit.elephant]
        o = [Officer(c, x, y) for c, x, y in cinit.officer]
        c = [Cannon(c, x, y) for c, x, y in cinit.cannon]
        self.chessboard = [['__' for i in range(9)] for i in range(10)]
        for ms in s, v, g, h, e, o, c:
            for m in ms:
                self.chessboard[m.x][m.y] = m


    def show(self):
        for i in range(10):
            print(self.line1.format(*self.chessboard[i]))
            if i == 4:
                print(self.line3)
            elif i != 9 :
                print(self.line2)



if __name__ == "__main__":
    l = Launch()
    l.initialization()
    l.show()